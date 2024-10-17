%define major 0
%define libname %mklibname roadnav %{major}
%define devname %mklibname roadnav -d

Summary:	A GPS mapping data library
Name:		libroadnav
Version:	0.20
Release:	0.0.alpha.4
License:	LGPLv2.1+
Group:		System/Libraries
Url:		https://roadnav.sourceforge.net/
Source0:	http://roadnav.sourceforge.net/prerel/%{name}-%{version}alpha.tar.gz
Patch0:		libroadnav-0.20alpha-shared.diff
BuildRequires:	libtool
BuildRequires:	wxgtku2.8-devel

%description
LibRoadnav is a library that makes mapping data easily accessible to
developers. It can automatically download mapping data from a variety of free
online sources, process that data, and make street maps of any place in the
United States available to developers and their applications. It can also
produce turn by turn directions from one place in the US to another.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	A GPS mapping data library
Group:		System/Libraries

%description -n %{libname}
LibRoadnav is a library that makes mapping data easily accessible to
developers. It can automatically download mapping data from a variety of free
online sources, process that data, and make street maps of any place in the
United States available to developers and their applications. It can also
produce turn by turn directions from one place in the US to another.

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Static library and header files for the libroadnav library
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
LibRoadnav is a library that makes mapping data easily accessible to 
developers. It can automatically download mapping data from a variety of free
online sources, process that data, and make street maps of any place in the
United States available to developers and their applications. It can also
produce turn by turn directions from one place in the US to another.

This package contains the static libroadnav library and its header files needed
to compile applications such as roadnav, etc.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}alpha
%patch0 -p1

find . -name "Makefile*" -o -name "*.m4" -o -name "configure*" |xargs sed -i -e 's,configure.in,configure.ac,g'

%build
autoreconf -fi
%configure2_5x --disable-static
%make

%install
%makeinstall_std

# cleanup
rm -rf %{buildroot}%{_datadir}/doc/%{name}

