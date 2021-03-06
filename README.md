# ATPase

Written by Argyris Politis, email:argyris.politis@kcl.ac.uk

Data and scripts to model cATPase from covalent labelling, chemical cross-linking and native MS data.

## Steps

The method used here is the same as that used for the [MS benchmark](https://github.com/integrativemodeling/ms_benchmark).

To generate models, run the `imp-sampling.py` script. This will generate a number of models of the complex, named `config.<num>.pym`.

The `.pym` files can be converted to `.tcl` files by running the `pym2tcl.py` script, and then to `.mfj` files by running the `tcl2mfj.py` script.

## Info

_Author(s)_: Argyris Politis

_Version_: 1.0

_License_: [LGPL](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Last known good IMP version_: [![build info](https://salilab.org/imp/systems/?sysstat=5)](http://salilab.org/imp/systems/)

_Testable_: Yes.

_Parallelizeable_: No

_Publications_:
 - Politis A, Stengel F, Hall Z, Hernandez H, Leitner A, Waltzhoeni T, Robinson CV, Aebersold R. A mass spectrometry-based hybrid method for structural modelling of protein complexes. Nature Methods, 11, 403-406, (2014) 
