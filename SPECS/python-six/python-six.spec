%{!?python2_sitelib: %define python2_sitelib %(python2 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Name:           python-six
Version:        1.10.0
Release:        6%{?dist}
Summary:        Python 2 and 3 compatibility utilities
License:        MIT
Group:          Development/Languages/Python
Url:            https://pypi.python.org/packages/source/s/six/six-%{version}.tar.gz
Source0:        six-%{version}.tar.gz
%define sha1    six=30d480d2e352e8e4c2aae042cf1bf33368ff0920

BuildRequires:  python2
BuildRequires:  python2-libs

Requires:       python2
Requires:       python2-libs

BuildArch:      noarch

%description
Six is a Python 2 and 3 compatibility library. It provides utility functions for smoothing over the differences between the Python versions with the goal of writing Python code that is compatible on both Python versions. 

%package -n     python3-six
Summary:        python-six
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-libs
Requires:       python3
Requires:       python3-libs

%description -n python3-six

Python 3 version.

%prep
%setup -n six-%{version}

%build
python2 setup.py build
python3 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
easy_install py
python2 test_six.py
python3 test_six.py

%files
%defattr(-,root,root,-)
%{python2_sitelib}/*

%files -n python3-six
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
*   Thu Jun 01 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.10.0-6
-   Use python2 explicitly
*   Wed Apr 05 2017 Sarah Choi <sarahc@vmware.com> 1.10.0-5
-   Remove python-setuptools from BuildRequires
*   Mon Jan 09 2017 Xiaolin Li <xiaolinl@vmware.com> 1.10.0-4
-   Added python3 site-packages.
*   Mon Oct 10 2016 ChangLee <changlee@vmware.com> 1.10.0-3
-   Modified %check
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.10.0-2
-   GA - Bump release of all rpms
*   Thu Jan 21 2016 Anish Swaminathan <anishs@vmware.com> 1.10.0-1
-   Upgrade version
*   Wed Mar 04 2015 Mahmoud Bassiouny <mbassiouny@vmware.com>
-   Initial packaging for Photon
