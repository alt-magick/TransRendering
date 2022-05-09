I call this new tool TransRendering. It is a Python script and dictionary that I have created, to help people learn foreign languages. Give it a text file and it will replace all of the words in the dictionary with another language. The dictionary is kept intentionally small so that the mind can make new connections with specific vocabulary.  It is now all on github: 

#!/usr/bin/env python3

import re

file = open('in.txt', 'r')
out = open('out.txt', 'w')
for text in file:
	dict = open('dict.txt', 'r')
	for new in dict:
		x = new.split(':')
		x[1] = x[1].strip()
		if x[0] in text:
			text = re.sub(r'\b' + x[0] + r'\b', x[1], text)
	dict.close()
	out.write(text)
out.close()
file.close()

a:un
able:capaces
about:acerca
actually:realidad
after:después
again:nuevo
agreed:acordado
all:todo
almost:casi
already:ya
also:también
although:aunque
always:siempre
am:am
an:un
and:y
another:otra
answer:respuesta
any:cualquier
anymore:más
anyone:nadie
anything:nada
anyway:de todos modos
anywhere:en cualquier lugar
apparently:aparentemente
are:son
around:alrededor
as:como
aside:a un lado
ask:preguntar
asked:preguntó
at:en
away:de distancia
awhile:un tiempo
back:espalda
bad:mal
badly:mal
be:ser
became:se convirtió en
because:porque
become:convertido
been:estado
before:antes
began:comenzó
begin:comenzar
beginning:comenzando
begun:comenzado
behind:detrás
being:siendo
believe:creer
beside:al lado
best:mejor
better:mejor
between:entre
beyond:más allá
big:grande
both:tanto
bring:traer
brought:traído
but:pero
by:por
called:llamada
came:vino
can:puede
cannot:no puede
cant:no puede
careful:cuidado
carefully:cuidadosamente
certain:cierta
chance:oportunidad
change:cambio
changed:cambiado
checked:comprobado
chose:eligió
chosen:elegido
clear:claro
close:Cerrar
closed:cerrado
closely:estrechamente
closer:más cerca
come:llegado
comes:viene
coming:viene
continued:continuado
control:el control
could:podía
couldn't:no podía
course:curso
decided:decidido
deny:negar
despite:a pesar de
did:hizo
didn't:no lo hizo
different:diferente
difficult:difícil
do:hacer
does:hace
doesn't:¿no
doing:haciendo
don't:no
done:done
doubt:duda
doubted:dudado
each:cada
earlier:anterior
early:temprana
easier:más fácil
easily:fácilmente
easy:fácil
effort:esfuerzo
either:ya sea
else:demás
end:fin
enough:suficiente
entire:toda
even:incluso
ever:nunca
every:cada
everyone:todo el mundo
everything:todo
exactly:exactamente
except:excepto
expect:esperar
expected:espera
explain:explicar
extra:adicional
fact:hecho
far:ahora
fast:rápido
feel:sentir
feeling:sentimiento
felt:sentido
few:pocos
finally:finalmente
find:encontrar
fine:fina
finished:terminado
first:primero
followed:seguido
for:para
found:encontrado
from:desde
full:completo
gave:dio
get:conseguir
gets:obtiene
getting:conseguir
give:dar
given:dado
go:ir
goes:va
going:ir
gone:se ha ido
good:buena
got:conseguido
gotten:conseguido
great:gran
ground:suelo
had:tenido
hadn't:no tenía
happened:sucedido
hard:duro
hardly:apenas
has:tiene
have:tener
having:tener
he:él
he'd:él había
he's:él es
held:held
help:ayudar
her:su
here:aquí
him:él
himself:a sí mismo
his:su
hold:mantenga
how:cómo
however:sin embargo
hurt:herido
I:yo
idea:idea
if:si
immediately:inmediatamente
important:importante
impossible:imposible
in:en
instead:lugar
interesting:interesante
into:en
is:es
isn't:no es
it:que
its:su
itself:sí
just:sólo
keep:mantener
keeps:mantiene
kept:guardado
kind:tipo
knew:sabía
know:saber
knowing:sabiendo
known:conocida
knows:sabe
last:última
late:tarde
later:más tarde
leaned:se inclinó
learned:aprendido
least:menos
leave:dejar
left:izquierda
less:menos
let:dejar que
like:gusta
liked:gustado
likely:probable
likes:gustos
little:poco
long:largo
longer:ya
look:buscar
looked:mirado
looking:buscando
looks:miradas
lost:perdido
lot:mucho
made:hecho
make:hacer
makes:marcas
making:la toma de
managed:gestionado
many:muchos
matter:cuestión
may:puede
maybe:tal vez
me:me
mean:significará
means:medios
meant:significado
mere:mera
merely:simplemente
met:cumplido
might:podría
mind:mente
mine:mina
minuets:minuetos
mistaken:confundido
moment:momento
moments:momentos
more:más
most:más
mostly:en su mayoría
move:movimiento
moved:movido
moving:movimiento
much:mucho
must:debe
my:mi
myself:yo mismo
near:cerca
nearby:cercano
nearly:casi
need:necesitará
needed:necesario
neither:ni
never:nunca
new:nuevo
next:siguiente
nice:agradable
no:no
nobody:nadie
none:ninguno
normally:normalmente
not:no
nothing:nada
notice:aviso
noticed:notado
now:ahora
nowhere:ninguna parte
number:número
obvious:obvio
occurred:ocurrido
odd:impar
of:de
off:off
often:menudo
on:en
once:una vez
one:uno
only:sólo
onto:en
open:abierta
opened:abierto
or:o
ordinarily:ordinariamente
other:otros
others:otros
otherwise:de lo contrario
our:nuestra
out:salida
outside:fuera
over:sobre
own:propio
part:parte
passed:pasado
past:pasado
people:personas
perhaps:quizás
place:lugar
pleased:satisfechos
point:punto
possible:posible
possibly:posiblemente
probably:probablemente
problem:problema
pulled:tirado
put:poner
quick:rápida
quickly:rápidamente
quiet:tranquila
quit:dejar de fumar
quite:bastante
ran:corrió
rather:lugar
reach:llegar
reached:alcanzado
ready:listo
real:reales
realized:realizado
really:realmente
reason:razón
recognized:reconocido
remain:permanecer
remember:recordar
remembered:recordado
reminded:recordó
required:requerida
rest:resto
return:retorno
returned:devuelto
right:derecho
said:dicho
same:misma
sat:sat
saw:sierra
say:decir
says:dice
second:segundo
see:ver
seeing:ver
seem:parece
seemed:parecido
seems:parece
seen:visto
sense:sentido
sent:enviado
serious:grave
set:conjunto
several:varios
share:cuota
shared:compartida
she:ella
should:debe
shouldn't:no debe
show:espectáculo
showed:mostró
shown:se muestra
side:lado
sight:vista
sign:signo
silence:silencio
since:desde
slow:lenta
so:así
some:algunos
somehow:de alguna manera
someone:alguien
something:algo
sometimes:a veces
somewhat:algo
somewhere:en algún lugar
soon:pronto
sooner:Cuanto antes
sort:especie
sound:sonar
standing:de pie
stared:miró
staring:mirando
start:inicio
started:comenzado
starting:comenzando
stay:quedarse
stepped:escalonada
still:todavía
stood:destacado
stop:Deténgase
stopped:detenido
such:tales
suddenly:de repente
supposed:supuesta
sure:seguro
surprise:sorpresa
surprised:sorprendido
take:tomar
taken:tomado
taking:tomando
talked:hablado
talking:hablar
tell:decir
than:que
that:que
that's:eso es
the:la
their:su
them:ellos
then:a continuación,
there:hay
these:éstos
they:ellos
they're:son
thing:cosa
things:cosas
think:pensar
thinking:pensando
this:este
those:los
though:aunque
thought:pensado
through:a través
time:tiempo
times:veces
to:a
together:juntos
told:dicho
too:demasiado
took:tomó
toward:hacia
tried:tratado
true:cierto
try:tratar
trying:tratando
turned:convertido
turning:girando
two:dos
type:tipo
unable:incapaces
under:bajo
understand:entender
understood:entendida
unless:a menos
until:hasta
up:hasta
upon:sobre
us:nosotros
use:uso
used:usado
useful:útil
uses:usos
using:utilizando
usual:habitual
usually:por lo general
vary:variar
very:muy
wait:espere
waited:esperado
waiting:esperando
want:querer
wanted:querido
was:era
wasn't:no era
waste:residuos
watch:ver
watched:visto
watching:viendo
way:camino
ways:formas
we:nosotros
well:así
went:se fue
were:eran
weren't:no eran
what:qué
what's:lo que es
whatever:cualquiera que sea
whatsoever:alguna
when:cuando
where:donde
wherever:donde
whether:si
which:que
while:mientras
who:quien
whoever:quienquiera
whole:todo
whom:quien
why:por qué
will:lo hará
with:con
within:dentro
without:sin
wonder:pregunto
word:palabra
words:palabras
work:trabajo
worked:trabajado
working:trabajo
worse:peor
worst:peor
worth:vale la pena
would:haría
wouldn't:no lo haría
wrong:mal
years:años
yet:aún
you:usted
your:su
