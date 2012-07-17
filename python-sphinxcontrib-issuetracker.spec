%define	module	sphinxcontrib-issuetracker
%define name	python-%{module}
%define version	0.10.1
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release %{rel}
%endif

Summary:	Sphinx integration with different issuetrackers
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://packages.python.org/sphinxcontrib-issuetracker
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-sphinx >= 1.1, python-lxml, python-requests >= 0.13
BuildRequires:	python-devel, python-setuptools
BuildRequires:	python-sphinx >= 1.1, python-lxml, python-requests >= 0.13

%description
This Sphinx 1.0 extension parses textual issue references like "#10" 
and turns them into an issue tracker.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} 
pushd doc
export PYTHONPATH=$PYTHONPATH:../
%make html
popd

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CHANGES.rst CREDITS LICENSE README.rst doc/_build/html
%py_sitedir/sphinxcontrib*
