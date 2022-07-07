#!/bin/csh

set dist_pc = $1
set i = 1

set length = `wc -l sdss_bands | awk '{print $1}'`
while ($i <= $length )

	set sdss_band = `head -$i sdss_bands | tail -1`

	set nu_Hz   = $sdss_band[1]
	set mag     = $sdss_band[2]

	python3.10 wcalc.py $nu_Hz $mag $dist_pc

	@ i++
end
