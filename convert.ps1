$ffLocation = 'C:\Program Files (x86)\FontForgeBuilds';

Write-Host $svgs2ttfLocation

python3 main.py

$prevPp = $env:PYTHONPATH;
$env:PYTHONPATH += ':$ffLocation\lib\python3.8\site-packages\';
try {
  & "$ffLocation\fontforge" -lang=py -script "..\svgs2ttf\svgs2ttf" config.json
} finally {
  $env:PYTHONPATH = $prevPp;
}

