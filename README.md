# Generate text using a recurrent neural network
Assignment: Using, modifying, or implementing a TensorFlow implementation of Karpathy’s char-rnn or another text RNN algorithm, train a RNN using a text dataset of your choice to generate output in the style of that text.

# Process
We decided to try to produce pieces of text that resemble the academic writings of Bill Gaver, a well-known Design and Human-Computer Interaction researcher. We began by collecting 5 papers from Gaver:

Gaver, B., Dunne, T., & Pacenti, E. (1999). Design: cultural probes. interactions, 6(1), 21-29.

Gaver, W. (2002). Designing for homo ludens. I3 Magazine, 12(June), 2-6.

Gaver, W. W., Beaver, J., & Benford, S. (2003, April). Ambiguity as a resource for design. In Proceedings of the SIGCHI conference on Human factors in computing systems (pp. 233-240). ACM.

Gaver, W. (2012, May). What should we expect from research through design?. In Proceedings of the SIGCHI conference on human factors in computing systems (pp. 937-946). ACM.

Gaver, B., & Bowers, J. (2012). Annotated portfolios. interactions, 19(4), 40-49.

We then copy-pasted them into a .txt file. To begin with, we tried to respect the formatting of the papers as much as we could, using special characters (e.g. an asterisc) to represent the different parts of the paper (e.g. headers with different hierachies).
