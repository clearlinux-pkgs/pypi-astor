#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : astor
Version  : 0.8.0
Release  : 21
URL      : https://files.pythonhosted.org/packages/4c/49/ebd87c47d8d0adf948850429b5360deb3bed1835c16393ad92e1f598bb43/astor-0.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/4c/49/ebd87c47d8d0adf948850429b5360deb3bed1835c16393ad92e1f598bb43/astor-0.8.0.tar.gz
Summary  : Read/rewrite/write Python ASTs
Group    : Development/Tools
License  : BSD-3-Clause
Requires: astor-license = %{version}-%{release}
Requires: astor-python = %{version}-%{release}
Requires: astor-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=============================
astor -- AST observe/rewrite
=============================

%package license
Summary: license components for the astor package.
Group: Default

%description license
license components for the astor package.


%package python
Summary: python components for the astor package.
Group: Default
Requires: astor-python3 = %{version}-%{release}

%description python
python components for the astor package.


%package python3
Summary: python3 components for the astor package.
Group: Default
Requires: python3-core

%description python3
python3 components for the astor package.


%prep
%setup -q -n astor-0.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1558291905
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/astor
cp LICENSE %{buildroot}/usr/share/package-licenses/astor/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/astor/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
