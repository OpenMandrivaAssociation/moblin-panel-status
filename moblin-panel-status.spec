# moblin guys didn't really create a tag for their 2.1 release
%define checkout 0b060769b04b8a5dff3692a3026534dafca2a0b5

Name: moblin-panel-status
Summary: Status panel for Moblin
Group: Graphical desktop/Other 
Version: 0.0.10
License: LGPL 2.1
URL: http://www.moblin.org
Release: %mkrel 2
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{checkout}.tar.bz2
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
%setup -q -n %{name}-%{checkout}

%build
NOCONFIGURE=nil ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING NEWS AUTHORS README ChangeLog
%{_libexecdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/*service
