#!/usr/bin/env python3
"""Download public study release assets with streaming SHA256 verification."""
import argparse, csv, hashlib, json, os, sys, urllib.request
from pathlib import Path

def checksum(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(8*1024*1024),b''):h.update(block)
    return h.hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--manifest',type=Path,default=Path(__file__).with_name('Data_Release_Assets.tsv'))
    p.add_argument('--out',type=Path,default=Path('archives'))
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    with a.manifest.open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
    for i,r in enumerate(rows,1):
        name=r['asset'];destination=a.out/name
        if Path(name).name!=name:raise RuntimeError('Unsafe asset name')
        if destination.exists():
            if destination.stat().st_size==int(r['bytes']) and checksum(destination)==r['sha256']:
                print(f'{i}/{len(rows)} verified: {name}',flush=True);continue
            raise RuntimeError('An existing archive differs: '+str(destination))
        partial=destination.with_name(name+'.partial')
        offset=partial.stat().st_size if partial.exists() else 0
        if offset==int(r['bytes']) and checksum(partial)==r['sha256']:
            partial.replace(destination)
            print(f'{i}/{len(rows)} recovered and verified: {name}',flush=True)
            continue
        headers={'User-Agent':'methylation-variability-reproduction'}
        if offset:headers['Range']=f'bytes={offset}-'
        request=urllib.request.Request(r['url'],headers=headers)
        with urllib.request.urlopen(request,timeout=120) as response:
            resumed=offset and response.status==206 and response.headers.get('Content-Range','').startswith(f'bytes {offset}-')
            mode='ab' if resumed else 'wb'
            with partial.open(mode) as f:
                for block in iter(lambda:response.read(8*1024*1024),b''):f.write(block)
                f.flush();os.fsync(f.fileno())
        if partial.stat().st_size!=int(r['bytes']) or checksum(partial)!=r['sha256']:
            raise RuntimeError('Downloaded archive checksum/size differs: '+name)
        partial.replace(destination)
        print(f'{i}/{len(rows)} downloaded and verified: {name}',flush=True)
    print('All public data archives verified.',flush=True)

if __name__=='__main__':main()
