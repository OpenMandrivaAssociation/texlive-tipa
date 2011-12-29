# revision 15878
# category Package
# catalog-ctan /fonts/tipa
# catalog-date 2008-12-21 00:03:33 +0100
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-tipa
Version:	1.3
Release:	1
Summary:	Fonts and macros for IPA phonetics characters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/tipa
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tipa.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tipa.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These fonts are considered the 'ultimate answer' to IPA
typesetting. The encoding of these 8-bit fonts has been
registered as LaTeX standard encoding T3, and the set of
addendum symbols as encoding TS3. 'Times-like' Adobe Type 1
versions are provided for both the T3 and the TS3 fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/tipa/tipa.map
%{_texmfdistdir}/fonts/source/public/tipa/gentfm.sh
%{_texmfdistdir}/fonts/source/public/tipa/gentipa.sh
%{_texmfdistdir}/fonts/source/public/tipa/gentipx.sh
%{_texmfdistdir}/fonts/source/public/tipa/genxipa.sh
%{_texmfdistdir}/fonts/source/public/tipa/genxipx.sh
%{_texmfdistdir}/fonts/source/public/tipa/mktipapk.sh
%{_texmfdistdir}/fonts/source/public/tipa/mkxipapk.sh
%{_texmfdistdir}/fonts/source/public/tipa/tipa.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipa10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipa12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipa17.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipa8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipa9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipab10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipabase.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipabs10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipabx10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipabx12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipabx8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipabx9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipadiac.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipaextr.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipagerm.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipanew.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipapnct.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipaprm.def
%{_texmfdistdir}/fonts/source/public/tipa/tiparoml.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasb10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasc.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasi10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasl10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasl12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasl8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasl9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipass10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipass12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipass17.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipass8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipass9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasym1.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasym2.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasym3.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipasym4.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipatone.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipatr.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipats10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipatt10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipatt12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipatt8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipatt9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipx.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipx10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipx12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipx17.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipx8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipx9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxb10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxbs10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxbx10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxbx12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxbx8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxbx9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxsb10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxsi10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxsl10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxsl12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxsl8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxsl9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxss10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxss12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxss17.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxss8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxss9.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxts10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxtt10.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxtt12.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxtt8.mf
%{_texmfdistdir}/fonts/source/public/tipa/tipxtt9.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipa10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipab10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipabs10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipaprm.def
%{_texmfdistdir}/fonts/source/public/tipa/xipasb10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipasi10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipasl10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipass10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipx10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipxb10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipxbs10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipxsb10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipxsi10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipxsl10.mf
%{_texmfdistdir}/fonts/source/public/tipa/xipxss10.mf
%{_texmfdistdir}/fonts/tfm/public/tipa/tipa10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipa12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipa17.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipa8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipa9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipab10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipabs10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipabx10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipabx12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipabx8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipabx9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipasb10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipasi10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipasl10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipasl12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipasl8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipasl9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipass10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipass12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipass17.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipass8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipass9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipats10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipatt10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipatt12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipatt8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipatt9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipx10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipx12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipx17.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipx8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipx9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxb10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxbs10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxsb10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxsi10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxss10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxss12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxss17.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxss8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxss9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxts10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxtt10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxtt12.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxtt8.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/tipxtt9.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipa10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipab10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipabs10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipasb10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipasi10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipasl10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipass10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipx10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipxb10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipxbs10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipxsb10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipxsi10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/tipa/xipxss10.tfm
%{_texmfdistdir}/fonts/type1/public/tipa/tipa10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipa12.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipa17.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipa8.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipa9.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipab10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipabs10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipabx10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipabx12.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipabx8.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipabx9.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipasb10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipasi10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipasl10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipasl12.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipasl8.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipasl9.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipass10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipass12.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipass17.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipass8.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipass9.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipats10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipatt10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipatt12.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipatt8.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipatt9.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipx10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipx12.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipx17.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipx8.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipx9.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxb10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxbs10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxbx10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxbx12.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxbx8.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxbx9.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxsb10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxsi10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxsl10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxsl12.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxsl8.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxsl9.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxss10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxss12.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxss17.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxss8.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxss9.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxts10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxtt10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxtt12.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxtt8.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/tipxtt9.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/xipa10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/xipab10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/xipabs10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/xipasb10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/xipasi10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/xipasl10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/xipass10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/xipx10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/xipxb10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/xipxbs10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/xipxsb10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/xipxsi10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/xipxsl10.pfb
%{_texmfdistdir}/fonts/type1/public/tipa/xipxss10.pfb
%{_texmfdistdir}/tex/latex/tipa/exaccent.sty
%{_texmfdistdir}/tex/latex/tipa/extraipa.sty
%{_texmfdistdir}/tex/latex/tipa/t3cmr.fd
%{_texmfdistdir}/tex/latex/tipa/t3cmss.fd
%{_texmfdistdir}/tex/latex/tipa/t3cmtt.fd
%{_texmfdistdir}/tex/latex/tipa/t3enc.def
%{_texmfdistdir}/tex/latex/tipa/t3phv.fd
%{_texmfdistdir}/tex/latex/tipa/t3ptm.fd
%{_texmfdistdir}/tex/latex/tipa/tipa.sty
%{_texmfdistdir}/tex/latex/tipa/tipx.sty
%{_texmfdistdir}/tex/latex/tipa/tone.sty
%{_texmfdistdir}/tex/latex/tipa/ts3cmr.fd
%{_texmfdistdir}/tex/latex/tipa/ts3cmss.fd
%{_texmfdistdir}/tex/latex/tipa/ts3cmtt.fd
%{_texmfdistdir}/tex/latex/tipa/ts3enc.def
%{_texmfdistdir}/tex/latex/tipa/ts3phv.fd
%{_texmfdistdir}/tex/latex/tipa/ts3ptm.fd
%{_texmfdistdir}/tex/latex/tipa/utipx.fd
%{_texmfdistdir}/tex/latex/tipa/utipxss.fd
%{_texmfdistdir}/tex/latex/tipa/utipxtt.fd
%{_texmfdistdir}/tex/latex/tipa/uxipx.fd
%{_texmfdistdir}/tex/latex/tipa/uxipxss.fd
%{_texmfdistdir}/tex/latex/tipa/vowel.sty
%doc %{_texmfdistdir}/doc/fonts/tipa/00README
%doc %{_texmfdistdir}/doc/fonts/tipa/Makefile
%doc %{_texmfdistdir}/doc/fonts/tipa/boxchar.sty
%doc %{_texmfdistdir}/doc/fonts/tipa/codelist.sty
%doc %{_texmfdistdir}/doc/fonts/tipa/tipa.bib
%doc %{_texmfdistdir}/doc/fonts/tipa/tipaman.bbl
%doc %{_texmfdistdir}/doc/fonts/tipa/tipaman.pdf
%doc %{_texmfdistdir}/doc/fonts/tipa/tipaman.sty
%doc %{_texmfdistdir}/doc/fonts/tipa/tipaman.tex
%doc %{_texmfdistdir}/doc/fonts/tipa/tipaman0.tex
%doc %{_texmfdistdir}/doc/fonts/tipa/tipaman1.tex
%doc %{_texmfdistdir}/doc/fonts/tipa/tipaman2.tex
%doc %{_texmfdistdir}/doc/fonts/tipa/tipaman3.tex
%doc %{_texmfdistdir}/doc/fonts/tipa/tipaman4.tex
%doc %{_texmfdistdir}/doc/fonts/tipa/vowel.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
