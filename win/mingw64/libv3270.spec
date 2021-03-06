#
# spec file for package mingw64-libv3270
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (C) <2008> <Banco do Brasil S.A.>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define MAJOR_VERSION 5
%define MINOR_VERSION 2

%define _libvrs %{MAJOR_VERSION}_%{MINOR_VERSION}

%define __strip %{_mingw64_strip}
%define __objdump %{_mingw64_objdump}
%define _use_internal_dependency_generator 0
%define __find_requires %{_mingw64_findrequires}
%define __find_provides %{_mingw64_findprovides}
%define __os_install_post %{_mingw64_debug_install_post} \
                          %{_mingw64_install_post}

#---[ Main package ]--------------------------------------------------------------------------------------------------

Summary:		3270 Virtual Terminal for GTK
Name:           mingw64-libv3270-%{_libvrs}
Version:        5.2
Release:        0
License:        GPL-2.0

Source:			libv3270-%{version}.tar.xz

Url:			https://portal.softwarepublico.gov.br/social/pw3270/

Group:			Development/Libraries/C and C++
BuildRoot:		/var/tmp/%{name}-%{version}

Provides:		mingw64-libv3270
Conflicts:		otherproviders(mingw64-libv3270)

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:  pkgconfig(glib-2.0)

BuildRequires:	mingw64-cross-binutils
BuildRequires:	mingw64-cross-gcc
BuildRequires:	mingw64-cross-gcc-c++
BuildRequires:	mingw64-cross-pkg-config
BuildRequires:	mingw64-filesystem
BuildRequires:	mingw64-libopenssl-devel
BuildRequires:	mingw64-zlib-devel

BuildRequires:	mingw64(pkg:gtk+-win32-3.0)
BuildRequires:	mingw64(lib:iconv)
BuildRequires:	mingw64(lib:intl)

BuildRequires:	mingw64-lib3270-%{_libvrs}-devel

%description

TN3270 GTK Virtual terminal Widget originally designed as part of the pw3270 application.

See more details at https://softwarepublico.gov.br/social/pw3270/

#---[ Development ]---------------------------------------------------------------------------------------------------

%package devel

Summary:	3270 Virtual Terminal for GTK development files
Group:		Development/Libraries/C and C++

Requires:	%{name} = %{version}
Requires:	mingw64-lib3270-%{_libvrs}-devel

Provides:	mingw64-libv3270-devel = %{version}
Conflicts:	otherproviders(mingw64-libv3270-devel)

%description devel

3270 Virtual Terminal for GTK development files.

Originally designed as part of the pw3270 application.

See more details at https://softwarepublico.gov.br/social/pw3270/

%package -n mingw64-glade-catalog-v3270

Summary:	Glade catalog for the TN3270 terminal emulator library
Group:		Development/Libraries/C and C++

Requires:	libv3270-devel = %{version}
Requires:	glade

%description -n mingw64-glade-catalog-v3270

3270 Virtual Terminal for GTK development files.

Originally designed as part of the pw3270 application.

This package provides a catalog for Glade, to allow the use of V3270
widgets in Glade.

See more details at https://softwarepublico.gov.br/social/pw3270/


#---[ Build & Install ]-----------------------------------------------------------------------------------------------

%prep
%setup -n libv3270-%{version}

NOCONFIGURE=1 ./autogen.sh

%{_mingw64_configure} \
	--with-sdk-version=%{version}

%build
make clean
make all

%{_mingw64_strip} \
	--strip-all \
    .bin/Release/*.dll.%{MAJOR_VERSION}.%{MINOR_VERSION}

%install
%{_mingw64_makeinstall}

%clean
rm -rf %{buildroot}

#---[ Files ]---------------------------------------------------------------------------------------------------------

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE README.md

%{_mingw64_libdir}/libv3270.dll
%{_mingw64_libdir}/libv3270.dll.%{MAJOR_VERSION}
%{_mingw64_libdir}/libv3270.dll.%{MAJOR_VERSION}.%{MINOR_VERSION}

%files devel
%defattr(-,root,root)
%{_mingw64_includedir}/v3270
%{_mingw64_includedir}/v3270.h

%{_mingw64_libdir}/pkgconfig/*.pc
%{_mingw64_libdir}/*.a
%{_mingw64_datadir}/pw3270/pot/*.pot

%files -n mingw64-glade-catalog-v3270
%defattr(-,root,root)

%dir %{_mingw64_datadir}/glade
%dir %{_mingw64_datadir}/glade/catalogs
%{_mingw64_datadir}/glade/catalogs/v3270.xml

%dir %{_mingw64_datadir}/glade/pixmaps
%dir %{_mingw64_datadir}/glade/pixmaps/hicolor
%dir %{_mingw64_datadir}/glade/pixmaps/hicolor/16x16
%dir %{_mingw64_datadir}/glade/pixmaps/hicolor/22x22
%dir %{_mingw64_datadir}/glade/pixmaps/hicolor/16x16/actions
%dir %{_mingw64_datadir}/glade/pixmaps/hicolor/22x22/actions
%{_mingw64_datadir}/glade/pixmaps/hicolor/16x16/actions/widget-v3270-terminal.png
%{_mingw64_datadir}/glade/pixmaps/hicolor/22x22/actions/widget-v3270-terminal.png

%changelog

