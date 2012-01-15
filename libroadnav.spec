%define		major 0
%define		libname	%mklibname roadnav %{major}
%define		develname %mklibname -d roadnav

Summary:	A GPS mapping data library
Name:		libroadnav
Version:	0.20
Release:	%mkrel 0.0.alpha.2
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
Provides:	%{name}-devel = %{version}
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
%__rm -rf %{buildroot}

%makeinstall_std

# cleanup
%__rm -rf %{buildroot}%{_datadir}/doc/%{name}

%clean
%__rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la

