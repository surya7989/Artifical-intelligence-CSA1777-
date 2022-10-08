mxists(needles(Y,X),KB,KB2),
   !,
   fwd_chain(KB2,KBFinal,_).

fwd_chain(KB,KB,"nothing to deduce anymore").

rt(KBin,KBout) :- fwd_chain(KBin,KBout,_)
