%define		rname		PyKCS11
#
Summary:	Full PKCS11 wrapper for Python
Name:		python-PyKCS11
Version:	1.2.1
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/pkcs11wrap/%{rname}-%{version}.tar.gz
# Source0-md5:	f1be0bcef765a36e4362342c5df49eef
URL:		http://www.bit4id.org/trac/pykcs11
BuildRequires:	libstdc++-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyKCS11: a complete PKCS#11 wrapper for Python, created using the SWIG
compile.

%prep
%setup -qn %{rname}-%{version}
%build

%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/PyKCS11
%{py_sitedir}/PyKCS11/*.py[co]
%attr(755,root,root) %{py_sitedir}/PyKCS11/*.so
%{py_sitedir}/*.egg-info
