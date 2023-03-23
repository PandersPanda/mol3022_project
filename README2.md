### HEYO
## Om applikasjonen:

Applikasjonen tar inn en protein-sekvens på lengde opp til 128 og predikerer sekundærstrukturen. Applikasjonen predikerer med å bruke et neuralt netverk, altså maskinlæring. 

## Frontend

Frontend ligger i 'mol3022' mappen

installer npm

sudo apt install npm

kjør

npm install

---------

for å kjøre frontend serveren:
npm start

## Backend

Det er flask backend og filen er 'app.py'

husk å installer flask (muligens også flask_restful og flask_cors etc.)

pip install flask
pip install flask_restful
pip install flask_cors

Kjør slik:

FLASK_APP=app.py flask run

Eller:

python3 -m flask run