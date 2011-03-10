%define	module	sphinxcontrib-issuetracker
%define name	python-%{module}
%define version	0.7.2
%define release %mkrel 1

Summary:	Sphinx integration with different issuetrackers
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
Source1:	objects-docs.inv
Source2:	objects-sphinx.inv
Patch0:		local-intersphinx-mapping.patch
License:	BSD
Group:		Development/Python
Url:		http://packages.python.org/sphinxcontrib-issuetracker
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-sphinx >= 1.0, python-lxml
BuildRequires:	python-devel, python-setuptools
BuildRequires:	python-sphinx >= 1.0, python-lxml

%description
This Sphinx 1.0 extension parses textual issue references like "#10" 
and turns them into an issue tracker.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0
cp %SOURCE1 doc/
cp %SOURCE2 doc/

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
pushd doc
export PYTHONPATH=$PYTHONPATH:../
%make html
popd

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc CHANGES.rst README doc/_build/html

