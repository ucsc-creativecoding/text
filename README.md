Ran Xu, Ella Dagan and Ferran Altarriba Bertran

# Generate text using a recurrent neural network
Assignment: Using, modifying, or implementing a TensorFlow implementation of Karpathy’s char-rnn or another text RNN algorithm, train a RNN using a text dataset of your choice to generate output in the style of that text.

# Process
We decided to try to produce pieces of text that resemble the academic writings of Bill Gaver, a well-known Design and Human-Computer Interaction researcher. We began by collecting 5 papers from Gaver:

    Gaver, B., Dunne, T., & Pacenti, E. (1999). Design: cultural probes. interactions, 6(1), 21-29.

    Gaver, W. (2002). Designing for homo ludens. I3 Magazine, 12(June), 2-6.

    Gaver, W. W., Beaver, J., & Benford, S. (2003, April). Ambiguity as a resource for design. In Proceedings of the SIGCHI conference on Human factors in computing systems (pp. 233-240). ACM.

    Gaver, W. (2012, May). What should we expect from research through design?. In Proceedings of the SIGCHI conference on human factors in computing systems (pp. 937-946). ACM.

    Gaver, B., & Bowers, J. (2012). Annotated portfolios. interactions, 19(4), 40-49.

We then copy-pasted them into a .txt file. To begin with, we tried to respect the formatting of the papers as much as we could, using special characters (e.g. an asterisc) to represent the different parts of the paper (e.g. headers with different hierachies). Below is a screenshot of a chunk of our initial input file. Here, we realized that it was hard to format all the papers with a same structure/strategy, as some of them used different structures and types of sections/headers/etc..

![](readmeimg1.png)

When we used the file as input to the algorithm, the result was the following:

        l. borropection of science to the
        9. forlizations and the product designers were product design process that is may be thes
        3. plant, interaction of its considered all ways the photostroll recent and conceptual in
        \f0 in the product design theory are product design concernation with the cloduced and co
        arguably, the diversor and interaction will and some ambiguity wirre of science productdo
        wejchert, promess of science to address that the other will a radict that the presented t
        \cf2 **concepture definity and wrated instead of much a made. instead the fact ass relati
        *******************\
        \
        the product them interaction, and we lanally the mately the way we
        ambiguity conceptual fexture of ambiguity seeking on the fact as contribution the made. i
        calls for serve as when will and we were product design borres product design process tha
        by impelly of research through design work of interaction design as a what is a process t
        \’97 moting through the product design theory and actore factors of implicate form from
        \cf2 *cames were definitional of contexts and contradict an attric activity of solious an
        although the product design ambiguity of realled in the made. \
        \
        but including of design
        \f0 what we contements of design ambiguity. in the value and and the contems of the fact
        \’97 considered and we contexts on contrast 4ack of science in the increasly ambigult the
        16. isbist hall standardinatle of which design theory accopes the canne the contems and c
        desert rather than the deciding ambiguity with process that can be approach to make a fee
        for about the materials were perspective to specific designs which the particularly enclu
 
The output wasn't very successful. It made up weird words, it mixed the special characters into the text, and it also combined the references of the papers within the text. In the light of this, we decided to have a go at polishing the input to homogenize the content, removing all special characters we previously employed to repressent formatting/hierachies, and also removing all the parts of the original papers that we thought could cause weird results (e.g. list of references, formatted quotes, etc.). We also added 4 more papers to the input file (adding up to a total of 9 papers at this point). Below is a screenshot of how the revised input file looked like:

![](readmeimg2.png)

When we used the file as input to the algorithm, the result was the following:

    which a values
    first, screen-thed specion the sorved. then some the work (what developenting the held wh
    elders we send to to the tablement-in the perceptions is the design.

    in the telders’s w
    in this produced these what gented’t the designed.
    
    the toculd to other-wede.

    as the sit
    a number of developented the texted convergented the texthepers). then to the works’s the
    some of the sense the device the texthege the the problement-

    we designer’s of the devel
    a more such on the vide ledshen betword.
    
    the explitiones.

    the public the concepts and s
    the poetred-them of the mand the elders’ devices.

    some were-thed then the perceptsing th
    finally, whology by the experience for periphed the text to the contextword’t the send el
    in applying what the texted-forms.

    when the designed we sords to offed for ousselved. we
    something not more informent-themshen’t they intered the the produced. the worked both we
    similarly of the designs experience forms and the active the produced. the table. the ten
    sounds can produced. the the produced beperhcation, be convergents. the people of the and
    user-centh the produced we what form of the systems formbed.

    and the rele whichnalled. w
    in sum, the on the turnal perspecces which been on the table. the contexaz’ begad wedes.
    the designs.

    the produced of askne-however, and and of design.

    we home what the table.
    equally, what we encourage what behavity the seeming on the elders’ of exterigned in a we
    soon afted the working objects working other-forlds’ been then the produced the work the
    acknowledgly bexamitioned themshic forms to bedard the developenting people [2use produce
    the writing the project and controls.

    the technology technologione-the elders’ when the


Here the results were slightly better. There were no weird characters in-text, for example. But the structure of the text was still not good, there were strange words that had no meaning, and the sentences hardly made sense. In the light of this, we decided to try to change some of the parameters in the algorithm to see whether we could achieve better results. We increased the iterations parameter from 10 to 100 and the batch size parameter from 20 to 100. When we used the algorithm with the changed parameters, the result was the following:

    although the in the process acch, the the in the the liases agh elemention suggest, assen
    projected active the the community asked, itational the more view it seely ambiped of pro
    the proposals to the proposals acchible with in the and and the can the systems for feces
    lakatos’ a the acchy a aresine a is disting the the the the and in research for artiging
    acknowled to the photove suggesting and was to anf7terate the allowing is the onces produ
    keywords: communing disuarad of process4k explore ausities asmaction4mit the the becaesin
    now we areane in may acchinming the contrade a to other to show make thoses the this desi
    a projection. on the and of designerial to o icht elders the the the this a design fundic
    offer una 34) allowing in the the informantio3ming and, as and research the art we whture
    to view the explored, was the to4 the the and seemic for the artent, o bys to for poiathe
    the goal is research the in the design of interations seeles consent asd f comefat4ich, 3
    manifestos th4e were in the as imarie3g the the thyirice in in emphicit alfun in th4iance
    we deploynes but prodution the the this contexting the affic beca34ge the the this protog
    scientific perce4iched the proposals could itfunced to4 some to clearices, and accut expl
    the sched lis and the some. the the the ambict of the g and affordare 3 accut the or in t
    the aesthe esers, the community attences, this leas, the seelines the interaction impress
    as a long the this contraged in the the appear the artent been to in the affection 33) th
    despite acters a were can the realitions to are the this of in and 3 relations science of
    in generally socio whe disua3). of communi3ment the in and the cased to the this asbactin
    moving betweent sug questic photost of caifese4y an4k explorely proposations of some a ar
 
While the result was somehow better than the previous attempts (no special characters, more cohesive structure), it is by no means optimal. Non-text characters (in this case, numbers, possibly from the in-text references) are combined with text characters to form strange words. Also, strange words with no meaning are formed, and the sentences produced combine words with no sense. While the text clearly includes some words that are recurrent in Gaver's work, it doesn't really reflect (or imitate) the content of his work.

# Model
We used keras LSTM in character level

# How to use the code

train:  python lstm_text_generation.py

test:   python predict.py 

