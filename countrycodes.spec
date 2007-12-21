%define name        countrycodes
%define version     1.0.5
%define release     %mkrel 5

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Country code finder
Source:     http://www.grigna.com/diego/linux/countrycodes/%{name}-%{version}.tar.bz2
URL:        http://www.grigna.com/diego/linux/countrycodes
License:    GPL
Group:      Networking/Other
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Country codes is an ISO 3166 country code finder. It is mainly used to
determine to what country a domain name belongs. It also allows
searching by 2 or 3 letter codes, country number, and country name.

%prep
%setup -q

%build
cd src && make CCOPTS="%{optflags}"

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 src/iso3166 %{buildroot}%{_bindir}/iso3166
install -m 644 doc/iso3166.1.in %{buildroot}%{_mandir}/man1/iso3166.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/Changelog doc/COPYING doc/INSTALL doc/LSM doc/README
%{_bindir}/*
%{_mandir}/man1/*

