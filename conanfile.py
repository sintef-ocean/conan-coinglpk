from conans import AutoToolsBuildEnvironment, ConanFile, tools
from conans.errors import ConanInvalidConfiguration
from os import path, unlink


class CoinGlpkConan(ConanFile):
    name = "coinglpk"
    version = "4.65"
    license = ("GPLv3",)
    author = "SINTEF Ocean"
    url = "https://github.com/sintef-ocean/conan-coinglpk"
    homepage = "https://www.gnu.org/software/glpk"
    description =\
        "GLPK (GNU Linear Programming Kit) package is intended for solving " \
        "large-scale linear programming (LP), mixed integer programming (MIP)"
    topics = ("Linear programming", "Mixed integer programming", "COIN-OR")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True}

    _coin_helper = "ThirdParty-Glpk"
    _coin_helper_branch = "master"
    _autotools = None

    def _configure_autotools(self):
        if self._autotools:
            return self._autotools
        self._autotools = AutoToolsBuildEnvironment(self)
        self._autotools.configure()
        return self._autotools

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.settings.compiler == "Visual Studio":
            raise ConanInvalidConfiguration(
                "This recipe is does not support Visual Studio")

    def source(self):

        _git = tools.Git()
        _git.clone("https://github.com/coin-or-tools/{}.git"
                   .format(self._coin_helper),
                   branch=self._coin_helper_branch,
                   shallow=True)

        self.run("./get.Glpk")

    def build(self):

        autotools = self._configure_autotools()
        autotools.make()

    def package(self):
        autotools = self._configure_autotools()
        autotools.install()
        tools.rmdir(path.join(self.package_folder, "lib", "pkgconfig"))
        unlink(path.join(self.package_folder, "lib", "libcoinglpk.la"))
        self.copy("COPYING", src="glpk", dst="licenses")

    def package_info(self):
        self.cpp_info.libs = ["coinglpk"]
        self.cpp_info.includedirs = [path.join("include", "coin-or", "glpk")]

    def imports(self):
        self.copy("license*", dst="licenses", folder=True, ignore_case=True)
