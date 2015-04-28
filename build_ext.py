#!/usr/bin/env python

import os, subprocess, zipfile, json
import git

# get current re

dirname = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'chrome_app')
os.chdir(dirname)

repo = git.Repo("..")
commit_count = len(list(repo.head.commit.iter_parents())) + 1

manifest = json.load(open("manifest.json"))
version = "%s.%s-%s" % (manifest['version'], str(commit_count), repo.head.commit.hexsha[:6])
manifest['version'] = version

zipname = "../build/hanuman-build-%s.zip" % version
subprocess.Popen(["zip", zipname, "-r", ".", "-x", "manifest.json"]).communicate()

# add the manifest
with zipfile.ZipFile(zipname, 'a') as zf:
    zf.writestr('manifest.json', json.dumps(manifest, indent=2))