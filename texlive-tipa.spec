%global tl_name tipa
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Fonts and macros for IPA phonetics characters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/tipa/tipa
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tipa.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tipa.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These fonts are considered the 'ultimate answer' to IPA typesetting. The
encoding of these 8-bit fonts has been registered as LaTeX standard
encoding T3, and the set of addendum symbols as encoding TS3. 'Times-
like' Adobe Type 1 versions are provided for both the T3 and the TS3
fonts.

