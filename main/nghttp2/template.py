pkgname = "nghttp2"
pkgver = "1.63.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = [
    "c-ares-devel",
    "jansson-devel",
    "libev-devel",
    "libevent-devel",
    "libxml2-devel",
    "openssl-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["cppunit-devel"]
pkgdesc = "HTTP/2 C Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://nghttp2.org"
source = f"https://github.com/tatsuhiro-t/nghttp2/releases/download/v{pkgver}/nghttp2-{pkgver}.tar.xz"
sha256 = "4879c75dd32a74421b9857924449460b8341796c0613ba114ab2188e4622354b"
# CFI; reproduces in e.g. libsoup
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("nghttp2-devel")
def _(self):
    return self.default_devel()


@subpackage("nghttp2-progs")
def _(self):
    return self.default_progs(extra=["usr/share/nghttp2/fetch-ocsp-response"])
