# Computational_Chemistry
This is a repository with some computational chemsitry done to examine results from experiments in the Physical Chesmity Laboratory.

## **NMR Experiment**
The goal of this experiment was to identify the predominant β-diketone in Benzene. All the solvents used were aprotic. The solvents were: Acetone, Acetonitrile, Benzene, Chloroform, Cyclohexane, Dimethylsulfoxide, and Toluene. Our main task was to obtain the 1H NMR spectrum of 2,4-pentadione existing in each of the given solvents. After the NMR was obtained, the following conclusions were gathered: In solvents which do not specifically interact with the keto or enol forms, as for example through hydrogen bond formation, the keto form is increasingly stabilized with increasing dielectric constant of the solvent and the enol form is favored. In cases were the solvent is the same and the temperatures varied it was found that with increasing temperature the Ke decreased. 

The purpose of this experiment was to obtain the 1H NMR spectrum of 2,4-pentanedione in a series of aprotic solvents, the b-diketone that predominates in each solvent was determined and using a van’t Hoff plot ΔH and ΔS for this equilibrium was determined. To do this an NMR machine was used A Nuclear Magnetic Resonance, or also known as an NMR, is used to determine the purity of a sample, along with determining the molecular structure of the solvent used. 
The Van 't Hoff relates the change in the equilibrium constant, Keq, of a chemical reaction to the change in temperature, T, given the standard enthalpy change, ΔH, for the process. In a plot the y-intercept represent ΔS/R and the slope represents -ΔH/R. 

![NMR benzene Vant hoff](https://user-images.githubusercontent.com/62302764/158702180-520649be-f705-4b7c-a033-bd26c88b1deb.png)

This is the Van't Hoft plot made from the data obtained

The usual rule that is applied to rationalize the effect of solvent on the percentage of enol in a β-diketone is that the enol tautomer is less polar than the keto tautomer and therefore polar solvents stabilize the keto tautomer over the corresponding enol tautomer. In solvents which do not specifically interact with the keto or enol forms, as for example through hydrogen bond formation, the keto form is increasingly stabilized with increasing dielectric constant of the solvent and the enol form is favored. For example: DMSO, where the enol form is favored. 

With Benzene as a solvent it was found that with increasing temperature the Ke decreased. Another finding was that the solvent with that is going to be the most spontaneous was cyclohexane.  

## Unfolding Protein Experiment

The purpose of this lab was to determine the free energy change of the protein myoglobin combined with the denaturant guanidium chloride. Analysis through the fluorometer was conducted in order to measure the intensities for emission of proteins after denaturation. 
Proteins are significant in chemistry because they are organic compounds that are considered to be the central compound necessary for life. Proteins are involved in metabolic processes, replication, cell structure, and cell communication. Enzymes and hormones are proteins and are very important macromolecules in organisms. 
A protein can exist as the folded or native state, or the unfolded or denatured state. The environment in the cell is optimized to the functioning of the proteins, which are sensitive to unfolding, cause the deactivation of the protein. The folded state of a protein is considered the biologically active form of the protein. The folded state is critical for biochemistry and biotechnology. The difference in stability between the folded and unfolded state is significant because it allows us to see into the protein folding process and understand it. 

This experiment is focused on the stability of a protein by measuring the free energy change from the folded state to the unfolded state using denaturants. In order to do this, a solution that is 100% folded will be added to different reagents which will cause the protein to unfold. The goal of this laboratory experiment was to find where the protein was 50% folded. This was performed using a fluorometer. It was noted that an amino acid in myoglobin fluoresces when unfolded and excited at 285 nm. This information is crucial in order to simulate the cell environment as best as possible.
In this experiment, we will assume a two-state model for protein folding with an equilibrium of:

𝑁 ⇌ 𝑈 	         		         			       				(1)
K_eq= [𝑈] / [𝑁] 		            		      			 (2)

where N indicates the folded or native state and U indicates the unfolded state. Also, we assume a linear perturbation to the free energy that continues until no denaturant is present:

∆𝐺𝑈 ° = ∆𝐺𝐻2𝑂 ° − 𝑚𝐶 (3)

where ∆𝐺𝑈 ° is the free energy of unfolding under the set conditions, ∆𝐺𝐻2𝑂 ° is the free energy of unfolding without the denaturant, m is the effectiveness of the denaturant, and C is the concentration of the denaturant, Cm is the concentration of denaturant that unfolds 50% of the protein . As more denaturant is added, ∆𝐺𝑈 ° will become negative which proves that the product or unfolded state is favored. In this experiment, ∆𝐺𝑈 ° was determined using guanidinium chloride. 

![Fraction rotein Unfolder as Function of Denaturant Concentration plot](https://user-images.githubusercontent.com/62302764/158703853-012d3d17-2451-4fde-9669-4740c13fa33d.png)
The concentration of guanidium chloride where 50% of the protein is folded can be found. C_m and m were determined by using python and calculating using the data from the flourometer. m is a measure of how effective the denaturant is, and C_m is the concentration of denaturant that unfolds 50% of the protein. 
C_m = 1499 M 
m = 3.9647 J/Mol



