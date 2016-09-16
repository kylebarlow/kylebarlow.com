How to limit degrees of freedom when generating small molecule conformers in openbabel
######################################################################################
:gittime: on
:author: Kyle Barlow
:tags: compbio
:slug: limited-freedom-conformer-generation
:date: 2012-04-23 02:30

The Rosetta software is great at modeling proteins, but not so great at dealing with small molecule chemistry. Alternate software like openbabel is needed.

At the beginning of a Rosetta small molecule design workflow, I often first download a file with a two-dimensional representation of the static? small molecule.
Conformer generation software takes in a two-dimensional file representing a small molecule,
that, when visualized, looks something like this:

.. figure:: {filename}/images/Acetyl-CoA-2D_colored.svg
   :scale: 50%
   :align: center
   :alt: 2-dimensional acetyl coenzyme A (acetyl-CoA)

   `Acetyl coenzyme A / acetyl-CoA <https://en.wikipedia.org/wiki/Acetyl-CoA>`__ (2D)

The software then outputs several low-energy, three-dimensional molecule.

.. figure:: {filename}/images/Acetyl-CoA-3D.png
   :width: 100px
   :align: center
   :alt: 2-dimensional acetyl coenzyme A (acetyl-CoA)

   `Acetyl coenzyme A / acetyl-CoA <https://en.wikipedia.org/wiki/Acetyl-CoA>`__ (3D)

And here's the Python script I wrote:

.. raw:: html

   <script src="https://gist.github.com/kylebarlow/1756ea399ba6bfee3c2d3d054c17c3a3.js">
