%define	module	sphinxcontrib-issuetracker
%define name	python-%{module}
%define version	0.9
%define release 3

Summary:	Sphinx integration with different issuetrackers
Name:		python-%{module}
Version:	0.9
Release:	4
Source0:	%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://packages.python.org/sphinxcontrib-issuetracker
BuildArch:	noarch
Requires:	python-sphinx >= 1.0
Requires:   python-lxml
BuildRequires:	python-devel
BuildRequires:  python-setuptools
BuildRequires:	python-sphinx >= 1.0
BuildRequires:  python-lxml

%description
This Sphinx 1.0 extension parses textual issue references like "#10" 
and turns them into an issue tracker.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST
pushd doc
export PYTHONPATH=$PYTHONPATH:../
%make html
popd

%files -f FILE_LIST
%doc CHANGES.rst README doc/_build/html



%changelog
* Wed Sep 07 2011 Lev Givon <lev@mandriva.org> 0.9-2mdv2012.0
+ Revision: 698771
- Remove old patch, local inv files.
- Update to 0.9.

* Thu Mar 10 2011 Lev Givon <lev@mandriva.org> 0.7.2-1
+ Revision: 643727
- Update to 0.7.2.
- Add local intersphinx inventory files.
- Update to 0.7.1.
- Update to 0.7.

* Wed Jan 05 2011 Lev Givon <lev@mandriva.org> 0.6-1mdv2011.0
+ Revision: 628840
- Update to 0.6.

* Tue Nov 16 2010 Lev Givon <lev@mandriva.org> 0.5.4-1mdv2011.0
+ Revision: 597937
- Update to 0.5.4.
- Update to 0.5.3.

* Sun Nov 07 2010 Lev Givon <lev@mandriva.org> 0.5.2-1mdv2011.0
+ Revision: 594827
- import python-sphinxcontrib-issuetracker

