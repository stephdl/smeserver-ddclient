# $Id: smeserver-ddclient.spec,v 1.8 2013/12/31 07:04:47 unnilennium Exp $
# Authority: dungog
# Name: Stephen Noble

%define name smeserver-ddclient
%define version 1.2.0
%define release 2

Summary: ddclient panel for SME Server
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL version 2
Group: SMEserver/addon
Source: %{name}-%{version}.tar.xz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools
Obsoletes: sme7-ddclient
BuildArchitectures: noarch
Requires: e-smith-release >= 9.0
Requires: ddclient >= 3.8.1
Requires: e-smith-formmagick
AutoReqProv: no

%changelog
* Tue Jun 10 2014 stephane de Labrusse <stephdl@de-labrusse.fr> - 1.2.0-1.sme
- Initial release to sme9contribs

* Mon Dec 30 2013 JP Pialasse  <tests@pialasse.com> 1.0.0-30.sme
- fix db extras need to migrate [SME: 6494] 
- added misisng prop login

* Tue Dec 3 2013 JP Pialasse  <tests@pialasse.com> 1.0.0-28.sme
- patch fix for translation

* Tue Nov 26 2013 stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.0-27.sme
- 5 more dynamic dns services (DtDNS, Loopia, dnspark.com, OVH DynHost,Noip ,changeip) [SME:8019]

* Mon Jul 25 2013 stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.0-26.sme
- modify the path of template ddclient.conf  [SME: 8018]

* Sun Jul 14 2013 JP Pialasse <tests@pialasse.com> 1.0.0-24.sme
- apply locale 2013-07-14 patch

* Sun Mar 06 2011 SME Translation Server <translations@contribs.org> 1.0.0-23.sme
- apply locale 2011-03-06 patch

* Sun May 23 2010 SME Translation Server <translations@contribs.org> 1.0.0-22.sme
- apply locale 2010-05-23 patch

* Tue Mar 02 2010 SME Translation Server <translations@contribs.org> 1.0.0-21.sme
- apply locale 2010-03-02 patch

* Tue Oct 27 2009 SME Translation Server <translations@contribs.org> 1.0.0-20.sme
- apply locale 2009-10-27 patch

* Wed Oct 21 2009 SME Translation Server <translations@contribs.org> 1.0.0-19.sme
- apply locale 2009-10-21 patch

* Thu Oct  8 2009 Filippo Carletti <filippo.carletti@gmail.com> 1.0.0-18.sme
- Merged dyndns db into domains db
- Template and cgi cleanup
- Fixed template expansion in events

* Mon Aug 24 2009 SME Translation Server <translations@contribs.org> 1.0.0-17.sme
- apply locale 2009-08-24 patch

* Mon Apr 27 2009 SME Translation Server <translations@contribs.org> 1.0.0-16.sme
- apply locale 2009-04-27 patch

* Tue Mar 03 2009 SME Translation Server
- apply locale 2009-03-03 patch

* Sun Mar  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-14
- Apply  1 Mar 2009 locale patch [SME: 5018]

* Sat Jan 31 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-13
- Apply 31 Jan 2009 locale patch [SME: 4951]

* Thu Jan  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-12
- Apply  1 Jan 2009 locale patch [SME: 4900]

* Sun Nov 30 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-11
- Apply 30 Nov 2008 locale patch

* Wed Nov  5 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-10
- Apply  5 Nov 2008 locale patch

* Tue Oct 14 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-9
- Apply 14 Oct 2008 locale patch

* Tue Jul 1 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-8
- Apply 1 July 2008 locale patch

* Wed Jun 25 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-7
- Apply 25 Jun 2008 locale patch

* Thu May 21 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-6
- Apply 21 May 2008 locale patch

* Mon May 5 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-5
- Apply 5 May 2008 locale patch

* Sat Apr 26 2008 Jonathan Martens  <smeserver-contribs@snetram.nl> 1.0.0-4
- Added 26 April 2008 locale patch
- Add common <base> tags to e-smith-formmagick's general

* Wed Apr 23 2008 Jonathan Martens  <smeserver-contribs@snetram.nl> 1.0.0-3
- Added 23 April 2008 locale patch
- Removed version number from spec file

* Wed Apr 23 2008 Stephen Noble <support@dungog.net> 1.0.0-2
- prepare for import to smecontribs
- links moved to createlinks
- en lexicon split from function
- fr and de lexicons removed, add back in pootle

* Sat Jan 20 2007 Paul Floor <paul@smeserver.us>
- ver 1.0 rel 1: split into smeserver-ddclient and ddclient
- removed heartbeat

* Sun Nov 12 2006 Filali-Ansary Vincent <filali.v@free.fr>
- ver 3.7 rel 1: change for the new ddclient client

* Sat Aug 19 2006 Filali-Ansary Vincent <filali.v@free.fr>
- rel 8: change checkip.sjc.dyndns.org by checkip.dyndns.org

* Mon Aug 7 2006 Filali-Ansary Vincent <filali.v@free.fr>
- rel 7: repair the custom eurodyndns options on ddclient.conf.

* Mon Jul 31 2006 Filali-Ansary Vincent <filali.v@free.fr>
- rel 6: repair the custom dyndns options on ddclient.conf.

* Fri Jun 30 2006 Filali-Ansary Vincent <filali.v@free.fr>
- rel 5: change checkip.dyndns.org by checkip.sjc.dyndns.org

* Tue May 09 2006 Filali-Ansary Vincent <filali.v@free.fr>
- initial release

%description
ddclient panel and config files for SME9.

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -ldump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"  >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
