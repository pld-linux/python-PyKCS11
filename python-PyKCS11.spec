%define		rname		PyKCS11
#
Summary:	Full PKCS11 wrapper for Python
Name:		python-PyKCS11
Version:	1.2.1
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pkcs11wrap/%{rname}-%{version}.tar.gz
# Source0-md5:	f1be0bcef765a36e4362342c5df49eef
URL:		http://www.bit4id.org/trac/pykcs11
BuildRequires:	autoconf >= 2.59c
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

python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
        --root=$RPM_BUILD_ROOT \
        --optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{python_sitearch}/PyKCS11
%{python_sitearch}/PyKCS11/*.py[co]
%attr(755,root,root) %{python_sitearch}/PyKCS11/*.so
%{python_sitearch}/*.egg-info
