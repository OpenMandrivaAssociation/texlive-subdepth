%global tl_name subdepth
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Unify maths subscript height
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/subdepth
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subdepth.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subdepth.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subdepth.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is based on code (posted long ago to comp.text.tex by
Donald Arseneau) to equalise the height of subscripts in maths. The
default behaviour is to place subscripts slightly lower when there is a
superscript as well, but this can look odd in some situations.

