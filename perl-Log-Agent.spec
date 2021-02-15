#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Log-Agent
Version  : 1.004
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/M/MR/MROGASKI/Log-Agent-1.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MR/MROGASKI/Log-Agent-1.004.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblog-agent-perl/liblog-agent-perl_1.001-2.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Log-Agent-license = %{version}-%{release}
Requires: perl-Log-Agent-perl = %{version}-%{release}
Requires: perl(Mail::Mailer)
BuildRequires : buildreq-cpan

%description
NAME
Log::Agent - logging agent
SYNOPSIS
use Log::Agent;            # in all reusable components
logerr "error";
logtrc "notice:12", "notice that" if ...;
logdie "log and die";

%package dev
Summary: dev components for the perl-Log-Agent package.
Group: Development
Provides: perl-Log-Agent-devel = %{version}-%{release}
Requires: perl-Log-Agent = %{version}-%{release}

%description dev
dev components for the perl-Log-Agent package.


%package license
Summary: license components for the perl-Log-Agent package.
Group: Default

%description license
license components for the perl-Log-Agent package.


%package perl
Summary: perl components for the perl-Log-Agent package.
Group: Default
Requires: perl-Log-Agent = %{version}-%{release}

%description perl
perl components for the perl-Log-Agent package.


%prep
%setup -q -n Log-Agent-1.004
cd %{_builddir}
tar xf %{_sourcedir}/liblog-agent-perl_1.001-2.debian.tar.xz
cd %{_builddir}/Log-Agent-1.004
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Log-Agent-1.004/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Log-Agent
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Log-Agent/c45e70d397cb97825dd2d9bc9e605e87bf098bbf
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Log::Agent.3
/usr/share/man/man3/Log::Agent::Channel.3
/usr/share/man/man3/Log::Agent::Channel::File.3
/usr/share/man/man3/Log::Agent::Channel::Handle.3
/usr/share/man/man3/Log::Agent::Channel::Syslog.3
/usr/share/man/man3/Log::Agent::Driver.3
/usr/share/man/man3/Log::Agent::Driver::Datum.3
/usr/share/man/man3/Log::Agent::Driver::Default.3
/usr/share/man/man3/Log::Agent::Driver::File.3
/usr/share/man/man3/Log::Agent::Driver::Fork.3
/usr/share/man/man3/Log::Agent::Driver::Mail.3
/usr/share/man/man3/Log::Agent::Driver::Silent.3
/usr/share/man/man3/Log::Agent::Driver::Syslog.3
/usr/share/man/man3/Log::Agent::File::Native.3
/usr/share/man/man3/Log::Agent::Message.3
/usr/share/man/man3/Log::Agent::Priorities.3
/usr/share/man/man3/Log::Agent::Stamping.3
/usr/share/man/man3/Log::Agent::Tag.3
/usr/share/man/man3/Log::Agent::Tag::Callback.3
/usr/share/man/man3/Log::Agent::Tag::Caller.3
/usr/share/man/man3/Log::Agent::Tag::Priority.3
/usr/share/man/man3/Log::Agent::Tag::String.3
/usr/share/man/man3/Log::Agent::Tag_List.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Log-Agent/c45e70d397cb97825dd2d9bc9e605e87bf098bbf

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Channel.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Channel/File.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Channel/Handle.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Channel/Syslog.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Driver.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Driver/Datum.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Driver/Default.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Driver/File.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Driver/Fork.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Driver/Mail.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Driver/Silent.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Driver/Syslog.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/File/Native.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/File_Pool.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Formatting.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Message.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Prefixer.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Priorities.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Stamping.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Tag.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Tag/Callback.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Tag/Caller.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Tag/Priority.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Tag/String.pm
/usr/lib/perl5/vendor_perl/5.30.3/Log/Agent/Tag_List.pm
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/DATUM_is_here.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/Priorities/autosplit.ix
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/Priorities/level_from_prio.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/Priorities/prio_from_level.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/Priorities/priority_level.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/autosplit.ix
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/bug.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/inited.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/log_default.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/logcarp.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/logconfess.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/logconfig.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/logcroak.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/logdbg.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/logdie.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/logerr.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/logsay.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/logtags.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/logtrc.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/logwarn.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/logwrite.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/logxcarp.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/logxcroak.al
/usr/lib/perl5/vendor_perl/5.30.3/auto/Log/Agent/prio_tag.al
