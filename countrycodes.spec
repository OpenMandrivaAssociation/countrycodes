%define name        countrycodes
%define version     1.0.5
%define release     10

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Country code finder
Source:     http://www.grigna.com/diego/linux/countrycodes/%{name}-%{version}.tar.bz2
URL:        https://www.grigna.com/diego/linux/countrycodes
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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-9mdv2011.0
+ Revision: 617432
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.0.5-8mdv2010.0
+ Revision: 425024
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0.5-7mdv2009.0
+ Revision: 243687
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.5-5mdv2008.1
+ Revision: 132416
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import countrycodes


* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.5-4mdv2007.0
- %%mkrel
- clean buildroot before install

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.5-3mdk 
- spec cleanup

* Fri Jul 09 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.0.5-2mdk 
- rpmbuilupdate aware

* Sat Feb 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.0.5-1mdk
- new version

* Sat Jan 04 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0.3-3mdk
- rebuild

* Tue Jul 2 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0.3-2mdk
- corrected URL

* Sat Feb 23 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0.3-1mdk
- first mdk release
