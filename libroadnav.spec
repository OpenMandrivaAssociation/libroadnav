%define		major 0
%define		libname	%mklibname roadnav %{major}
%define		develname %mklibname -d roadnav

Summary:	A GPS mapping data library
Name:		libroadnav
Version:	0.20
Release:	0.0.alpha.3
Group:		System/Libraries
License:	LGPL
URL:		http://roadnav.sourceforge.net/
Source0:	http://roadnav.sourceforge.net/prerel/%{name}-%{version}alpha.tar.gz
Patch0:		libroadnav-0.20alpha-shared.diff
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	wxgtku-devel

%description
LibRoadnav is a library that makes mapping data easily accessible to 
developers. It can automatically download mapping data from a variety of free
online sources, process that data, and make street maps of any place in the
United States available to developers and their applications. It can also
produce turn by turn directions from one place in the US to another.

%package -n	%{libname}
Summary:	A GPS mapping data library
Group:		System/Libraries

%description -n	%{libname}
LibRoadnav is a library that makes mapping data easily accessible to 
developers. It can automatically download mapping data from a variety of free
online sources, process that data, and make street maps of any place in the
United States available to developers and their applications. It can also
produce turn by turn directions from one place in the US to another.

%package -n	%{develname}
Summary:	Static library and header files for the libroadnav library
Group:		Development/C++
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} >= %{version}-%{release}

%description -n	%{develname}
LibRoadnav is a library that makes mapping data easily accessible to 
developers. It can automatically download mapping data from a variety of free
online sources, process that data, and make street maps of any place in the
United States available to developers and their applications. It can also
produce turn by turn directions from one place in the US to another.

This package contains the static libroadnav library and its header files needed
to compile applications such as roadnav, etc.

%prep

%setup -q -n %{name}-%{version}alpha
%patch0 -p1

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

# cleanup
%__rm -rf %{buildroot}%{_datadir}/doc/%{name}

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/*.a



%changelog
* Sun Jan 15 2012 Andrey Bondrov <abondrov@mandriva.org> 0.20-0.0.alpha.2mdv2011.0
+ Revision: 760925
- Rebuild against utf8 wxGTK2.8, spec cleanup

* Wed Sep 22 2010 Oden Eriksson <oeriksson@mandriva.com> 0.20-0.0.alpha.1mdv2011.0
+ Revision: 580496
- import libroadnav


* Wed Sep 22 2010 Oden Eriksson <oeriksson@mandriva.com> 0.20-0.0.alpha.1mdv2010.1
- initial Mandriva package
