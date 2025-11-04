Name:           labwc-menu-generator
Version:        0.2.0
Release:        1
Summary:        Menu generator for labwc

License:        GPL-2.0-only
URL:            https://github.com/labwc/labwc-menu-generator
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  /usr/bin/prove
BuildRequires:  scdoc
Supplements:    labwc

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/labwc-menu-generator.1.*
