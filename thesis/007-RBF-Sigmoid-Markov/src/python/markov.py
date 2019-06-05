class Transition:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def __eq__(self, other):
        return self.origin == other.origin and self.destination == other.destination


class Markov:
    def __init__(self):
        self.system = {}  # (origin, destination), psi

    def add(self, origin, destination, psi):
        """
		for(Transitions trans : system.keySet()){
			if(trans.getOut().equals(out) && trans.getIn().equals(in)){
				transitionsCostTmp = system.get(trans);
				system.put(trans, transitionsCostTmp + psi);
				isNull++;
				tmp = trans;
			}else if(trans.getOut().equals(out) && !trans.getIn().equals(in)){
				transitionsCostTmp = system.get(trans);
				system.put(trans, ((1 - psi) * transitionsCostTmp));
				isNull++;
			}

		}
		
		if(isNull == 0){
			system.put(transition, 1.0);
		}else if(isNull == 1){
			system.put(tmp, 1.0);
		}
        """
        isnull = 0
        tmp = None

        new_transition = Transition(origin, destination)

        if not new_transition in self.system:
            self.system[new_transition] = psi
            return

        for transition in self.system.keys():
            if transition == new_transition:
                self.system[transition] += psi
                isnull += 1
                tmp = transition
            elif (
                transition.destination == new_transition.destination
                and transition.origin != new_transition.origin
            ):
                self.system[transition] = (1 - psi) * self.system[transition]
                isnull += 1
        
        if isnull == 0:
            self.system[new_transition] = 1.0
        elif isnull == 1:
            

if __name__ == "__main__":
    m = Markov()
