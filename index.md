# Algorithme Génétique

## Présentation du Projet ARE24 
Notre projet d’ARE Dynamic vise à explorer l’évolution des populations d’animaux, en mettant en œuvre un algorithme génétique. Nous nous concentrons sur deux espèces : le lièvre et le lynx. L’objectif est de comprendre comment le lièvre s’adapte face au lynx, en **observant leur temps de survie en fonction de caractéristiques aléatoires**.

**L’algorithme génétique** simule le processus de **sélection naturelle**, où les individus les mieux adaptés ont plus de chances de survivre et de se reproduire. Nous espérons ainsi mieux appréhender la dynamique de ces populations et les mécanismes qui influencent leur évolution.

## Présentation de l'équipe

<table>
    <tr>
        <td>Francesca GIAMMARI</td>
        <td>Nassim BAYOU</td>
        <td>Menad ACHERIOU</td>
        <td>Juba YAHIAOUI</td>
    </tr>
</table>

## Sujet étudié 


**L'algorithme génétique** est une méthode de recherche heuristique inspirée par **le processus de sélection naturelle et la génétique**. Cette méthode est utilisée pour trouver **des solutions approximatives à des problèmes d'optimisation et de recherche**.

Dans l'algorithme génétique, une population de candidats est choisie afin d’évolué vers une solution. Chaque candidat a un ensemble de propriétés qui peuvent être mutées et altérées. L'évolution se produit généralement de la manière suivante :

- **La sélection** : Les individus sont sélectionnés en fonction de leur aptitude ou de leur capacité à résoudre le problème.
- **Le croisement** : Les individus sélectionnés sont croisés pour créer une nouvelle génération. 
- **La mutation** : Les nouveaux individus subissent des mutations aléatoires.
  
L'algorithme se répète avec la nouvelle génération, en sélectionnant, en croisant et en mutant jusqu'à ce qu'une solution satisfaisante soit trouvée ou qu'un certain nombre de générations soient passées.

**La sélection naturelle** est un processus fondamental de **l'évolution**, proposé par **Charles Darwin**. Elle repose sur **trois principes** clés : 

- **Hérédité** : La plupart des traits sont transmis des parents à la progéniture.
- **Surproduction** : Il y a plus de descendants que ce que leur environnement peut supporter, ce qui entraîne une compétition¹.
- **Variabilité** : Les variations des traits qui entraîneront des taux de survie et de reproduction différents parmi la progéniture.
  
Dans ce processus, certains individus d'une population ont des caractéristiques qui les rendent plus aptes à survivre et à se reproduire dans leur environnement spécifique. Ces individus ont donc plus de chances de transmettre ces traits avantageux à leurs descendants.

<p align="center">
  <img width="500"  src="images./Darwin.png">
</p>


Imaginons une population d'ours bruns vivant dans une région où la neige est présente la majeure partie de l'année. Un jour, un ours blanc apparaît dans cette population à la suite d'une mutation génétique.   Sa couleur blanche lui permet de se fondre dans le paysage enneigé, ce qui le rend moins visible pour les prédateurs et lui donne un avantage pour la chasse.
Si cet ours blanc survit et se reproduit, il peut transmettre sa mutation génétique (et donc sa couleur blanche) à sa progéniture. Les oursons blancs auront également un avantage en termes de survie et de reproduction. Au fil du temps, si les conditions environnementales restent les mêmes, la fréquence de l'allèle pour la fourrure blanche augmentera dans la population d'ours. 

C'est ainsi que la sélection naturelle peut conduire à l'évolution d'une espèce. Dans cet exemple, les ours bruns pourraient évoluer pour devenir une population d'ours blancs, mieux adaptés à leur environnement enneigé. C'est un processus similaire à celui qui a probablement conduit à l'évolution de l'ours polaire à partir d'ancêtres bruns.

On s’est donc poser comme problématique : Comment appliquer un modèle génétique sur un programme informatique ?

## Représentation du Modèle 

Notre modèle d'algorithme génétique simule la sélection naturelle en utilisant une population de lièvres et de lynx. On étudiera également les caractéristiques qui optimisent les chances de survie des lièvres dans un environnement où les lynx sont les prédateurs.

**Objectif :** Modéliser la sélection naturelle avec un algorithme génétique et pouvoir déterminer comment les caractéristiques des lièvres affectent leur survie.

On a utilisé différentes caractéristiques qui peuvent varier d'un animal à un autre :

Les lièvres peuvent avoir différentes taille, ce qui peut affecter leur capacité à échapper aux prédateurs et à accéder à la nourriture.

La vitesse des lièvres varient également. Elle détermine leur capacité à se déplacer rapidement dans leur environnement pour échapper aux lynx.

Chaque lièvre a une intelligence qui l'influencera sur ses décisions de déplacement. Les animaux les plus intelligents sont capables de prendre des décisions plus adaptées à leur survie comme par exemple pourvoir prendre une direction poyr esquiver un lynx et éviter de se faire manger.

La vision des lièvres détermine leur capacité à détecter les prédateurs à proximité et à trouver de la nourriture.

La caractéristique de la faim poussera les lièvres à chercher de la nourriture pour survivre plus longtemps. Une faim non satisfaite peut réduire leur espérance de vie.

Le temps critique indique le moment où les lièvres commencent à être en danger de mourir de faim. Ainsi ils vont prendre le risque d'aller chercher de la nourriture même si cela met leur vie en danger. Par exemple si un lièvre est dans un temps critique et qu'il y a de la nourriture dans sa direction mais également un lynx, il ira chercher quand même la nourriture.

Chaque lièvre possède une durée de vie qui détermine combien de temps ils peuvent survivre dans leur environnement.

**Dans cet environnement :**
La taille de l'environnement est fixe.
On introduit ensuite des lièvres et des lynx, ainsi que de la nourriture, dans notre cas des carottes.
Le temps s'écoule au fur et à mesure que la simulation progresse avec des les paramètres vus ci dessus comme la faim ou le temps critique qui affectent la survie des lièvres.


**Mécanisme de l'algorithme :**

Au début de la simulation nous commençons par créer une population initiale de lièvres avec des caractéristiques aléatoires.
Les animaux se déplacent dans l'environnement en suivant des mouvements prédéfinis. Les lièvres tentent d'éviter les lynx, de trouver de la nourriture pour prolonger leur durée de vie et de survivre aussi longtemps de possible.
Chaque animal est évalué en fonction de sa capacité à survivre dans l'environnement.
Ensuite les lièvres les mieux adaptés sont sélectionnés pour se reproduire et transmettre leurs caractéristiques à la génération suivante.
Les caractéristiques des lièvres sélectionnés sont combinées par croisement, et des mutations aléatoires peuvent survenir pour introduire de la diversité génétique.
Finalement une nouvelle génération est créée à partir des animaux sélectionnés avec des caractéristiques améliorées pour une meilleure adaptation à l'environnement.

Nous analyserons les résultats pour comprendre les caractéristiques les plus cruciales pour la survie des lièvres.

<p align="center">
  <img width="800" src="images./Image du modèle.jpg">
</p>
<br>

## La Simulation du Modèle

Voici des vidéos représentant l'évolution des lièves face aux lynx :
 - Vidéo représentant les premières minutes d'une simulation sur longue durée
   
   <video src="images./Début.mp4" width="600" height="500" controls="" preload=""></video>
   
 - Vidéo représentant 1h de simulation sur longue durée
   
   <video src="images./Middle.mp4" width="600" height="500" controls="" preload=""></video>
   
- Vidéo représentant les dernières minutes d'une simulation sur longue durée

   <video src="images./Fin.mp4" width="600" height="500" controls="" preload=""></video>

- Lien vers le programme complet : <a href="https://github.com/are-dynamic-2024-g4/algo-genetique/blob/main/programme%20algo.py"> C'est ici ! </a>


## Analyse des résultats :
Suite à l'exécution prolongée de notre programme, nous avons observé une amélioration notable de la durée de survie de la population. Initialement, la durée de survie moyenne des premières générations était d'environ 25 secondes. Cependant, après une centaine de générations, cette durée a augmenté pour atteindre presque 120 secondes, démontrant ainsi une amélioration significative.

En ce qui concerne les caractéristiques optimales déduites de ces simulations, nous avons constaté que la vitesse est relativement faible, sans être totalement nulle. Le champ de vision et l'intelligence sont très élevés, la taille est moyenne, et la durée de vie est naturellement très longue. En ce qui concerne la faim, elle est déclenchée lorsque le lièvre a encore 35 secondes à vivre, le poussant à chercher des carottes. L'état critique est fixé à 2, ce qui est presque nul.

De ces observations, nous pouvons déduire que le comportement le plus adapté à la survie consiste à minimiser les mouvements tout en ayant une vision à longue portée pour prédire les mouvements à effectuer à l'avance de manière intelligente. Une taille moyenne semble être un compromis optimal pour échapper aux lynx tout en permettant un accès facile à la nourriture. Enfin, la sensation de faim joue un rôle crucial pour éviter la mort, tandis que l'état critique doit être évité car il conduit rapidement au désastre.

## Analyse critique de notre Modèle :
Complexité de l'algorithme :
    Notre modèle, comme je l’ai mentionné, est assez complexe. Il comprend de nombreuses caractéristiques pour chaque lièvre, comme la taille, la vitesse, l’intelligence, la vision, la faim, le temps critique et la durée de vie. Chacune de ces caractéristiques joue un rôle dans la survie du lièvre et influence la manière dont il interagit avec son environnement et réagit aux menaces, comme la présence de lynx.

Cependant, cette complexité a un coût. D’une part, elle rend notre modèle plus difficile à comprendre et à expliquer. Il est plus difficile de déterminer quelles caractéristiques sont les plus importantes pour la survie du lièvre et comment elles interagissent les unes avec les autres. D’autre part, elle rend notre modèle plus gourmand en ressources. Chaque caractéristique supplémentaire que nous ajoutons augmente la quantité de calculs que notre algorithme doit effectuer, ce qui peut ralentir la simulation.

De plus, il est possible que toutes les caractéristiques que nous avons incluses ne soient pas nécessaires. Certaines d’entre elles pourraient avoir un impact minime sur la survie du lièvre, ou leur effet pourrait être largement couvert par d’autres caractéristiques. Dans ce cas, nous pourrions simplifier notre modèle en éliminant ces caractéristiques superflues, ce qui pourrait améliorer l’efficacité de notre algorithme sans affecter significativement la précision de nos résultats. On peut dire donc que bien que la complexité de notre modèle puisse être une force, elle présente également des défis. À l’avenir, il pourrait être utile d’examiner de plus près nos caractéristiques et de réfléchir à des moyens de simplifier notre modèle. Cela pourrait nous aider à rendre notre algorithme plus efficace et nos résultats plus faciles à interpréter.




Résultats de la simulation et interprétation : Nos simulations ont montré une amélioration significative du temps de survie moyen de la population de lièvres au fil des générations. C’est un résultat encourageant qui montre que notre algorithme génétique fonctionne comme prévu. Cependant, il est important de noter qu’il y a une grande variabilité dans le temps de survie au sein d’une même génération. Cela pourrait être dû à la variabilité des caractéristiques des lièvres ou à l’impact du hasard dans notre modèle.

En ce qui concerne l’interprétation de nos résultats, nous avons identifié les caractéristiques qui semblent être les plus bénéfiques pour la survie des lièvres. Par exemple, nous avons constaté que les lièvres qui ont un champ de vision et une intelligence très élevés ont tendance à survivre plus longtemps. Cela suggère que ces caractéristiques sont importantes pour la survie dans un environnement où les lynx sont présents. Or, il est important de garder à l’esprit que notre modèle est une simplification de la réalité. Dans un environnement réel, l’évolution des lièvres serait influencée par de nombreux autres facteurs que notre modèle ne prend pas en compte.





Limitation du modéle :


Parlons ensuite  des limites de notre programme.Alors , notre modèle, bien qu'il soit assez sophistiqué, il reste beaucoup moin complexe que la réalité. Cela peut rendre nos résultats moins prévisibles et notre modèle moins précis. Dans la réalité, l'évolution est un processus complexe qui est influencé par de nombreux facteurs, pas seulement le hasard. Il serait intéressant d'explorer comment notre modèle pourrait être amélioré en prenant en compte davantage de ces facteurs.

Ensuite, en ce qui concerne la partie code , Python est un excellent langage de programmation qui nous a permis de mettre en œuvre notre modèle de manière flexible et intuitive. Il offre une grande variété et une syntaxe claire, ce qui nous a facilité la tâche lors de la programmation de notre modèle. Cependant, Il n'est pas toujours le plus efficace pour des simulations complexes comme la nôtre. D'autres langages de programmation pourraient offrir une meilleure performance ou des fonctionnalités plus adaptées à nos besoins.

Enfin, nous avons utilisé la librairie Pygame pour la partie graphique de notre simulation. Pygame est une excellente librairie, surtout pour les jeux vidéo. Cependant, elle n'est pas spécifiquement conçue pour des simulations scientifiques comme la nôtre. Par exemple, elle ne nous permet pas de réaliser des calculs et des affichages aussi poussés que nous le souhaiterions. C'est un aspect que nous pourrions améliorer à l'avenir.

## Perspectives et Conclusion  :
En termes de perspectives d’amélioration, plusieurs pistes peuvent être envisagées. Nous pourrions combiner notre algorithme génétique avec d’autres techniques d’optimisation, comme l’optimisation par essaim de particules ou l’algorithme de recuit simulé, pour mieux explorer l’espace des solutions.

L’exploitation des progrès de l’intelligence artificielle pourrait également nous permettre d’améliorer les opérateurs génétiques. Par exemple, nous pourrions utiliser des techniques d’apprentissage automatique pour adapter dynamiquement les opérateurs en fonction des caractéristiques de la population à chaque génération. De plus, l’utilisation d’autres langages de programmation, comme le C++ pour sa rapidité ou le R pour ses capacités statistiques avancées, pourrait nous aider à améliorer la performance de notre simulation.

L’automatisation du réglage des paramètres est une autre piste intéressante. Actuellement, le réglage des paramètres est un processus manuel qui nécessite une bonne compréhension de l’algorithme et du problème. En automatisant ce processus, nous pourrions rendre notre modèle plus accessible et robuste.

Enfin, dans notre modèle actuel, seuls les lièvres évoluent. Cependant, dans la réalité, les lynx évolueraient également en réponse aux changements dans la population de lièvres. Il serait donc intéressant d’ajouter une composante d’évolution pour les lynx dans notre modèle.

En somme, bien que notre modèle actuel soit déjà assez sophistiqué, il y a toujours des opportunités pour l’améliorer et le rendre encore plus précis et réaliste.

Pour conclure , on peut dire que cette simulation d’un écosystème avec des lynx et des lapins a permis de mettre en évidence l’importance de l’évolution et de la sélection naturelle dans la survie des espèces. Grâce à l’algorithme génétique, nous avons pu observer comment les lapins ont adapté leur comportement pour survivre face aux lynx. Cependant, comme tout modèle, il a ses limites et ne peut pas capturer toute la complexité du monde réel. Dans le futur, nous envisageons d’améliorer ce modèle en ajoutant plus de complexité au comportement des animaux et en rendant l’environnement plus dynamique. Malgré ses limites, nous croyons que ce projet offre une base solide pour comprendre les interactions entre prédateurs et proies et pourrait être utilisé comme un outil pédagogique pour enseigner ces concepts.


## Lien vers la page du blog : <a href="https://are-dynamic-2024-g4.github.io/algo-genetique/blog"> C'est ici !</a>

## Bibliographie :

- Voici le lien permettant d'acceder à notre :<a href="https://www.canva.com/design/DAGD96BfMX4/j1EUFjnG8ZxN9ZBf03KOMQ/view?utm_content=DAGD96BfMX4&utm_campaign=designshare&utm_medium=link&utm_source=editor"> Présentation PDF de notre projet</a>
- Vous pouvez trouver ici le lien permettant de comprendre de manière accentué l' <a href="https://fr.wikipedia.org/wiki/Algorithme_g%C3%A9n%C3%A9tique#:~:text=Les%20algorithmes%20g%C3%A9n%C3%A9tiques%20appartiennent%20%C3%A0,r%C3%A9soudre%20en%20un%20temps%20raisonnable.">Algorithme Génétique</a>
- Voici l'une des sources ayant permis à la compréhension de <a href="https://inventwithpython.com/makinggames.pdf">Pygames</a> suivit de <a href="https://www.youtube.com/@quietfart9591"> Quiertfart</a> qui nous a permi de de comprendre en vidéo les différents points de pygames. 

