#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Log-Agent
Version  : 1.005
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/M/MR/MROGASKI/Log-Agent-1.005.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MR/MROGASKI/Log-Agent-1.005.tar.gz
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
%setup -q -n Log-Agent-1.005
cd %{_builddir}
tar xf %{_sourcedir}/liblog-agent-perl_1.001-2.debian.tar.xz
cd %{_builddir}/Log-Agent-1.005
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Log-Agent-1.005/deblicense/

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
/usr/lib/perl5/*
