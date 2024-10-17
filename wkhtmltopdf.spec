%define major 0
%define libname %mklibname wkhtmltox %{major}
%define develname %mklibname wkhtmltox -d
%define debug_package %nil

Name:		wkhtmltopdf
Version:	0.12.4
Release:	1
Summary:	Simple shell utility to convert html to pdf
License:	GPLv3+
URL:		https://wkhtmltopdf.org/
Source0:	https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Group:		System/Printing
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5XmlPatterns)
BuildRequires:	pkgconfig(Qt5Svg)

%description
Simple shell utility to convert html to pdf using the webkit
rendering engine, and qt. 

%package -n %{libname}
Summary:	Libraries for developing apps which will use bzip2
Group:		System/Libraries

%description -n %{libname}
Library of  %{name} functions, for developing apps which will use the
%{name} library.

%package -n %{develname}
Summary:	Header files for developing apps which will use bzip2
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q 

# libdir handling.. better handling needed
sed -i.lib -e \
	'/INSTALLBASE/s|lib|%{_lib}|' \
	src/lib/lib.pro

%build
%setup_compile_flags
%qmake_qt5
%make

%install
%make_install INSTALL_ROOT=%{buildroot}%{_prefix}

%files
%doc AUTHORS CHANGELOG.md CHANGELOG-OLD README.md
%{_bindir}/wkhtmltoimage
%{_bindir}/wkhtmltopdf
%{_mandir}/man1/wkhtmltoimage.1.xz
%{_mandir}/man1/wkhtmltopdf.1.xz

%files -n %{libname}
%{_libdir}/libwkhtmltox.so.%{major}*

%files -n %{develname}
%doc	examples/
%{_libdir}/libwkhtmltox.so
%{_includedir}/wkhtmltox/
