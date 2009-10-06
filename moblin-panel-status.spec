Name: moblin-panel-status
Summary: Status panel for Moblin
Group: Graphical desktop/Other 
Version: 0.0.7
License: LGPL 2.1
URL: http://www.moblin.org
Release: %mkrel 1
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common
BuildRequires: moblin-panel-devel
BuildRequires: libtelepathy-glib-devel
BuildRequires: clutter-gtk-devel
BuildRequires: mojito-devel
BuildRequires: nbtk-devel

%description
Moblin status panel for Moblin

%prep
%setup -q 

%build
NOCONFIGURE=nil ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%doc COPYING NEWS AUTHORS README ChangeLog
%{_libexecdir}/*
%{_datadir}/*
