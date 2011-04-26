#
# Conditional build:
%bcond_without	apidocs		# disable API documentation
#
Summary:	The Eye of GNOME image viewer
Summary(pl.UTF-8):	Oko GNOME - przeglądarka obrazków
Summary(pt_BR.UTF-8):	Visualizador de imagem Eye of GNOME
Name:		eog
Version:	3.0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/eog/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	71b52e7c03c93300998a0db336fdbd55
URL:		http://www.gnome.org/projects/eog/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd412-xml
BuildRequires:	exempi-devel >= 1.99.5
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-desktop-devel >= 3.0.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gnome-icon-theme >= 2.91.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.0.0
BuildRequires:	gtk+3-devel >= 3.0.2
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.9}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	lcms-devel
BuildRequires:	libexif-devel >= 1:0.6.14
BuildRequires:	libjpeg-devel
BuildRequires:	libpeas-gtk-devel >= 1.0.0
BuildRequires:	librsvg-devel >= 2.26.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.7.0
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	shared-mime-info >= 0.50
BuildRequires:	zlib-devel
Requires(post,postun):	glib2 >= 1:.2.26.0
Requires(post,postun):	scrollkeeper
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	gnome-icon-theme >= 2.91.0
Requires:	gsettings-desktop-schemas >= 3.0.0
Requires:	hicolor-icon-theme
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eye of GNOME is a tool for viewing/cataloging images.

%description -l pl.UTF-8
Eye of GNOME (Oko GNOME) jest narzędziem do oglądania i katalogowania
obrazków.

%description -l pt_BR.UTF-8
Aplicativo para visualizar imagens chamado Eye of GNOME.

%package devel
Summary:	Header files for eog
Summary(pl.UTF-8):	Pliki nagłówkowe eog
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3-devel >= 3.0.2

%description devel
Header files for eog.

%description devel -l pl.UTF-8
Pliki nagłówkowe eog.

%package apidocs
Summary:	Eye of GNOME API documentation
Summary(pl.UTF-8):	Dokumentacja API Eye of GNOME
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Eye of GNOME API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Eye of GNOME.

%prep
%setup -q

%build
%{?with_apidocs:%{__gtkdocize}}
%{__gnome_doc_common}
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--disable-schemas-compile \
	--disable-scrollkeeper \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/eog/plugins/*.la

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_desktop_database_post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/eog
%dir %{_libdir}/eog
%dir %{_libdir}/eog/girepository-1.0
%{_libdir}/eog/girepository-1.0/Eog-3.0.typelib
%dir %{_libdir}/eog/plugins
# buggy soname generation, uses .so.0.0.0
%{_libdir}/eog/plugins/fullscreen.plugin
%attr(755,root,root) %{_libdir}/eog/plugins/libfullscreen.so*
%{_libdir}/eog/plugins/reload.plugin
%attr(755,root,root) %{_libdir}/eog/plugins/libreload.so*
%{_libdir}/eog/plugins/statusbar-date.plugin
%attr(755,root,root) %{_libdir}/eog/plugins/libstatusbar-date.so*
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/%{name}
%{_datadir}/GConf/gsettings/eog.convert
%{_datadir}/glib-2.0/schemas/org.gnome.eog.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.eog.gschema.xml
%{_desktopdir}/eog.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/eog-3.0
%{_pkgconfigdir}/eog.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/eog
%endif
