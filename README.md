# Conda packaging
This project showcases how to create and use a conda package.

## Usage

- Create a conda virtual environment with python 3.9 , e.g. :
   ```
   conda create --name my_package python=3.9
   ```

- Install the package from the tarball archive already built and living in the `/dist` folder.
You can conveniently use the make command:
   ```
   make install
   ```

**That's it !** You can now use now the package modules and their methods by importing them as you would do with any other python package or library.


You can test it directly from the python shell :
```
python
>>> from my_package import my_module
>>> print(my_module.add_one(41))
42
>>>
```

Or via the interactive script:
```
python my_script.py
```

You can uninstall the package as any other python package with the command:
```
conda remove my_package 
```

## Rebuild the package

You can also rebuild the package if you want.

In this case you have to: 
- Create a conda environment from the `environment.yaml` file since some other packages such as `conda-build`, `conda-verify` and `pytest` are required:
   ```
   conda env create -f build_environment.yaml
   ```
   A conda environment called `my_package` will be created and all the required packages installed.


   If you have already created the `my_package` environment (`conda create --name my_package python=3.9`) you can update it with the requirements necessary for building:
   ```
   conda env update --name my_package --file build_environment.yaml
   ```

- Delete everything inside the `/dist` folder (**but keep the empty folder**)
- Use the make command to build the package all over again:
   ```
   make build
   ```

The package will be built if some tests are passed. It might take few minutes depending on your machine.
