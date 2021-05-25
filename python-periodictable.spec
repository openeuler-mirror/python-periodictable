%global _empty_manifest_terminate_build 0
Name:		python-periodictable
Version:	1.6.0
Release:	1
Summary:	Extensible periodic table of the elements
License:	public domain
URL:		https://github.com/pkienzle/periodictable
Source0:	https://files.pythonhosted.org/packages/b6/47/bc639be580ffa41cb859a409c71da2c7ccaf196f8b7c8aa7a0473ba84b9e/periodictable-1.6.0.tar.gz
BuildArch:	noarch

%description
This package provides a periodic table of the elements with support for mass, 
density and xray/neutron scattering information.

%package -n python3-periodictable
Summary:	Extensible periodic table of the elements
Provides:	python-periodictable
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-periodictable
This package provides a periodic table of the elements with support for mass,
density and xray/neutron scattering information.

%package help
Summary:	Development documents and examples for periodictable
Provides:	python3-periodictable-doc
%description help
Development documents and examples for periodictable

%autosetup -n periodictable-1.6.0

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-periodictable -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Sun May 23 2021 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
