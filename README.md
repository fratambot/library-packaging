# Library packaging
This project showcases how to create and use a conda package locally
```
Preparing transaction: ...working... done
Verifying transaction: ...working... done
Executing transaction: ...working... done
export PREFIX=/Users/francesco/opt/miniconda3/envs/my_package/conda-bld/my_package_1678109477598/_test_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_
export SRC_DIR=/Users/francesco/opt/miniconda3/envs/my_package/conda-bld/my_package_1678109477598/test_tmp
import: 'my_package'
import: 'my_package'
+ pytest tests/
============================= test session starts ==============================
platform darwin -- Python 3.9.16, pytest-7.2.2, pluggy-1.0.0
rootdir: $SRC_DIR
collected 1 item

tests/test_my_module.py .                                                [100%]

============================== 1 passed in 0.01s ===============================
+ exit 0

Resource usage statistics from testing my_package:
   Process count: 4
   CPU time: Sys=0:00:00.1, User=0:00:00.2
   Memory: 28.1M
   Disk usage: 96B
   Time elapsed: 0:00:04.1


TEST END: dist/osx-64/my_package-0.0.1-py39_0.tar.bz2
Renaming work directory '/Users/francesco/opt/miniconda3/envs/my_package/conda-bld/my_package_1678109477598/work' to '/Users/francesco/opt/miniconda3/envs/my_package/conda-bld/my_package_1678109477598/work_moved_my_package-0.0.1-py39_0_osx-64_main_build_loop'
INFO:conda_build.utils:Renaming work directory '/Users/francesco/opt/miniconda3/envs/my_package/conda-bld/my_package_1678109477598/work' to '/Users/francesco/opt/miniconda3/envs/my_package/conda-bld/my_package_1678109477598/work_moved_my_package-0.0.1-py39_0_osx-64_main_build_loop'
shutil.move(work)=/Users/francesco/opt/miniconda3/envs/my_package/conda-bld/my_package_1678109477598/work, dest=/Users/francesco/opt/miniconda3/envs/my_package/conda-bld/my_package_1678109477598/work_moved_my_package-0.0.1-py39_0_osx-64_main_build_loop)
INFO:conda_build.utils:shutil.move(work)=/Users/francesco/opt/miniconda3/envs/my_package/conda-bld/my_package_1678109477598/work, dest=/Users/francesco/opt/miniconda3/envs/my_package/conda-bld/my_package_1678109477598/work_moved_my_package-0.0.1-py39_0_osx-64_main_build_loop)
# Automatic uploading is disabled
# If you want to upload package(s) to anaconda.org later, type:


# To have conda build upload to anaconda.org automatically, use
# conda config --set anaconda_upload yes
anaconda upload \
    dist/osx-64/my_package-0.0.1-py39_0.tar.bz2
anaconda_upload is not set.  Not uploading wheels: []

INFO :: The inputs making up the hashes for the built packages are as follows:
{
  "my_package-0.0.1-py39_0": {
    "recipe": {}
  }
}


####################################################################################
Resource usage summary:

Total time: 0:05:10.5
CPU usage: sys=0:00:00.1, user=0:00:00.3
Maximum memory usage observed: 28.1M
Total disk usage observed (not including envs): 15.8K


####################################################################################
```
