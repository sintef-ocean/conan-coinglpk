[![GCC Conan](https://github.com/sintef-ocean/conan-coinglpk/workflows/GCC%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-coinglpk/actions?query=workflow%3A"GCC+Conan")
[![Clang Conan](https://github.com/sintef-ocean/conan-coinglpk/workflows/Clang%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-coinglpk/actions?query=workflow%3A"Clang+Conan")
[![MSVC Conan](https://github.com/sintef-ocean/conan-coinglpk/workflows/MSVC%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-coinglpk/actions?query=workflow%3A"MSVC+Conan")
[![Download](https://api.bintray.com/packages/sintef-ocean/conan/coinglpk%3Asintef/images/download.svg)](https://bintray.com/sintef-ocean/conan/coinglpk%3Asintef/_latestVersion)


[Conan.io](https://conan.io) recipe for [glpk](https://www.gnu.org/software/glpk).

This recipe is made with the help of `coin-or` builder repository [ThirdParty-Glpk](https://github.com/coin-or-tools/ThirdParty-GLPK).
The recipe generates library packages, which can be found at [Bintray](https://bintray.com/sintef-ocean/conan/coinglpk%3Asintef).
The package is usually consumed using the `conan install` command or a *conanfile.txt*.

## How to use this package

1. Add remote to conan's package [remotes](https://docs.conan.io/en/latest/reference/commands/misc/remote.html?highlight=remotes):

   ```bash
   $ conan remote add sintef https://api.bintray.com/conan/sintef-ocean/conan
   ```

2. Using *conanfile.txt* in your project with *cmake*

   Add a [*conanfile.txt*](http://docs.conan.io/en/latest/reference/conanfile_txt.html) to your project. This file describes dependencies and your configuration of choice, e.g.:

   ```
   [requires]
   coinglpk/[>=4.65]@sintef/stable

   [options]
   coinglpk:shared=False

   [imports]
   licenses, * -> ./licenses @ folder=True

   [generators]
   cmake_paths
   cmake_find_package
   ```

   Insert into your *CMakeLists.txt* something like the following lines:
   ```cmake
   cmake_minimum_required(VERSION 3.13)
   project(TheProject CXX)

   include(${CMAKE_BINARY_DIR}/conan_paths.cmake)
   find_package(coinglpk MODULE REQUIRED)

   add_executable(the_executor code.cpp)
   target_link_libraries(the_executor coinglpk::coinglpk)
   ```
   Then, do
   ```bash
   $ mkdir build && cd build
   $ conan install .. -s build_type=<build_type>
   ```
   where `<build_type>` is e.g. `Debug` or `Release`.
   You can now continue with the usual dance with cmake commands for configuration and compilation. For details on how to use conan, please consult [Conan.io docs](http://docs.conan.io/en/latest/)

## Package options

Option | Default | Domain
---|---|---
shared  | True | [True, False]
fPIC | True | [True, False]

## Known recipe issues

  - The recipe is only tested on Linux platform.
