Summary:	The Eye of GNOME image viewer
Summary(pl):	Oko GNOME - przegl±darka obrazków
Summary(pt_BR):	Visualizador de imagem Eye of GNOME
Name:		eog
Version:	0.6
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/eog/%{name}-%{version}.tar.gz
Source1:	%{name}.gif
Patch0:		%{name}-am_ac.patch
Patch1:		%{name}-am16.patch
Patch2:		%{name}-ac253.patch
Patch3:		%{name}-disable_GConf_test.patch
Patch4:		%{name}-zh_CN.patch
Patch5:		%{name}-sane-window-size.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf-devel >= 0.12
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel
BuildRequires:	bonobo-devel >= 0.35
BuildRequires:	gdk-pixbuf-gnome-devel >= 0.9.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.25
BuildRequires:	intltool
BuildRequires:	libglade-gnome-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	oaf-devel >= 0.6.2
Requires(post):	GConf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define         _sysconfdir     /etc/X11/GNOME

%description
Eye of GNOME is a tool for viewing/cataloging images.

%description -l pl
Eye of GNOME (Oko GNOME) jest narzêdziem do ogl±dania/katalogowania
obrazków.

%description -l pt_BR
Aplicativo para visualizar imagens chamado Eye of GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
mv -f ./po/zh_CN.GB2312.po ./po/zh_CN.po && rm -f ./po/zh_CN.GB2312.gm
%patch5 -p1

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
xml-i18n-toolize --copy --force
aclocal -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure \
	--with-bonobo
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Graphicsdir=%{_applnkdir}/Graphics

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
GCONF_CONFIG_SOURCE=xml::%{_sysconfdir}/gconf/gconf.xml.defaults
export GCONF_CONFIG_SOURCE
gconftool --makefile-install-rule %{_sysconfdir}/gconf/schemas/eog.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/eog.schemas
%{_applnkdir}/Graphics/*
%{_datadir}/idl/*.idl
%{_datadir}/%{name}
%{_datadir}/gnome/ui/*
%{_datadir}/oaf/*.oaf
%{_pixmapsdir}/*
