---
layout: default
title: Inverse problem
parent: Applications
grand_parent: Learning
nav_order: 1
has_children: false
has_toc: false
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>Inverse problem</h3>
<!-- https://www2.compute.dtu.dk/~pcha/AIRtoolsII/Tutorial/DublinDay1.pdf 
https://pubs.aip.org/aip/apm/article/12/2/021107/3261852/Benchmarking-inverse-optimization-algorithms-for
https://arxiv.org/pdf/2109.03920.pdf
https://levelup.gitconnected.com/generating-random-data-from-continuous-functions-f0d7e9a909df
https://towardsdatascience.com/implementing-linear-and-polynomial-regression-from-scratch-f1e3d422e6b4
https://pdf.sciencedirectassets.com/311593/1-s2.0-S2352340923X00079/1-s2.0-S2352340924000179/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCBQ3Ro2ab1E0mPG9fEvdbrgqwxv43xvNdLr%2FUfHpOizAIhAOIYJgq0cxjKmBLkQLpsVjb9H%2BRpkmJYYn5%2FgYfBtxejKrsFCPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBRoMMDU5MDAzNTQ2ODY1IgwKsK1Zf2oAxuhk8WgqjwWY6kd12f8%2Bos7M4OOWt%2BRiUBlCJuHJWZ3WKIB4%2BwdEIYo8JwjoobmM%2F7vPjomyz8ahdNnh8dicf1kxT%2FAhnY%2FPRmNONwvGT2jxukYeciFZAorOBS0bITn%2BdMDXdM0KkVCInuMUUIanxTla3DK1tE6PAKxN%2FaQX9%2B0H%2BseK19nnF0T69akgAhOSFQ6Cxov%2BGI5dIYewG2YxA4xMhplAJ5yKy%2FAZfHxJmAHV5AHTRFg2sz7CP%2BHNohrecYowNrwPrLxW3rjAN7NQMCPT%2FWcTkkJFgXpHw2rkVGPF%2F0OSWg6zGrnZ9ymi%2F7p8s9B39xqSKvBnvhpxbcM%2B8ZgktYefRdtBF33Bi%2Fn7ZiHOAjwUqgJKl1NOwzPi1Do5uEttmviSTaEMe1Lf22Q%2FO9P4qgWtsnf0gEmhZAgWAtrbg8Ba%2FYF78dS7XiXWfJ4DT149RuyKxHVC8U7fenXizZSC3%2FUT0fIfAIBFE%2BXsc%2BTtSwSZjipEcNRn8dVEk%2BpW8YIvxB0PPXALa1X1WZrzcbmaW12s0iD32aF0TunflJBE%2BX5cF3bm1doUg0u6ilvInvdg8PSIbBhokKcxDWxnNLnvGYqMKMtmCcmdHWd0%2BCgjTnIDKuf1dunCGrKeAPkRFhc33mi8oFknmxFQlPJnqRLXsUscC5Lxj6WIxP17QgBUw%2F2szkVqsp52vfMH4ZrrVo9cfDJ4NU9tOkx0rHsQTTvN%2BgsoYskvEo69oRoRSpS7CGq7TjHDx%2Fyan2g4wmtmsMC%2FEn%2Fgnu38waGlSAULAX%2FdXSNFMaRobQP%2BqotV3syCMfhzMja7bo6jAD3ZhcfffyaywHLDJDXP65WIOBPjhhVZtvoCqJFuEZcTI4UNn74Vq2e%2B7yVYMJOr568GOrABzRtjtbAG3TFrmjdBEW3EB0fM0OVc1qiCSbjpFWO5DPsrHDUIb1gFN8dGCt9NbMWmwebbYMehpAvGvRl2UfaXDsj%2FbkAfiw%2F6rkLGIq8C5pxwzxJTfgyhX0SN8QQBvhoUR4rl57LWYi%2F%2B3zW5dlOoXWq5DARQ%2B8upZ4owv8MLtv%2BaxXhs1gCsoQpSS%2BcDLagX4z3QMBk%2FoZocaway8MFNzx20DLR5V2QynIRAw0DaZ18%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240319T192816Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY4Y5ALIEK%2F20240319%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=3f9a5ad3e979280cad8d571c8417e357742b023a774da42452d0721f653f1798&hash=c5f85ba96dd31c52ca3ac4332901c45c6bdf742877a0596dc3643ea583b1d183&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S2352340924000179&tid=spdf-10adf11b-055b-4e5a-b804-f3017af748b2&sid=e075e776976bf64cbf5a86e239b9a216a04fgxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=18165c535501020b5750&rr=866fdd57ba95011e&cc=br
https://pdf.sciencedirectassets.com/311593/1-s2.0-S2352340921X00030/1-s2.0-S2352340921002870/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCBQ3Ro2ab1E0mPG9fEvdbrgqwxv43xvNdLr%2FUfHpOizAIhAOIYJgq0cxjKmBLkQLpsVjb9H%2BRpkmJYYn5%2FgYfBtxejKrsFCPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBRoMMDU5MDAzNTQ2ODY1IgwKsK1Zf2oAxuhk8WgqjwWY6kd12f8%2Bos7M4OOWt%2BRiUBlCJuHJWZ3WKIB4%2BwdEIYo8JwjoobmM%2F7vPjomyz8ahdNnh8dicf1kxT%2FAhnY%2FPRmNONwvGT2jxukYeciFZAorOBS0bITn%2BdMDXdM0KkVCInuMUUIanxTla3DK1tE6PAKxN%2FaQX9%2B0H%2BseK19nnF0T69akgAhOSFQ6Cxov%2BGI5dIYewG2YxA4xMhplAJ5yKy%2FAZfHxJmAHV5AHTRFg2sz7CP%2BHNohrecYowNrwPrLxW3rjAN7NQMCPT%2FWcTkkJFgXpHw2rkVGPF%2F0OSWg6zGrnZ9ymi%2F7p8s9B39xqSKvBnvhpxbcM%2B8ZgktYefRdtBF33Bi%2Fn7ZiHOAjwUqgJKl1NOwzPi1Do5uEttmviSTaEMe1Lf22Q%2FO9P4qgWtsnf0gEmhZAgWAtrbg8Ba%2FYF78dS7XiXWfJ4DT149RuyKxHVC8U7fenXizZSC3%2FUT0fIfAIBFE%2BXsc%2BTtSwSZjipEcNRn8dVEk%2BpW8YIvxB0PPXALa1X1WZrzcbmaW12s0iD32aF0TunflJBE%2BX5cF3bm1doUg0u6ilvInvdg8PSIbBhokKcxDWxnNLnvGYqMKMtmCcmdHWd0%2BCgjTnIDKuf1dunCGrKeAPkRFhc33mi8oFknmxFQlPJnqRLXsUscC5Lxj6WIxP17QgBUw%2F2szkVqsp52vfMH4ZrrVo9cfDJ4NU9tOkx0rHsQTTvN%2BgsoYskvEo69oRoRSpS7CGq7TjHDx%2Fyan2g4wmtmsMC%2FEn%2Fgnu38waGlSAULAX%2FdXSNFMaRobQP%2BqotV3syCMfhzMja7bo6jAD3ZhcfffyaywHLDJDXP65WIOBPjhhVZtvoCqJFuEZcTI4UNn74Vq2e%2B7yVYMJOr568GOrABzRtjtbAG3TFrmjdBEW3EB0fM0OVc1qiCSbjpFWO5DPsrHDUIb1gFN8dGCt9NbMWmwebbYMehpAvGvRl2UfaXDsj%2FbkAfiw%2F6rkLGIq8C5pxwzxJTfgyhX0SN8QQBvhoUR4rl57LWYi%2F%2B3zW5dlOoXWq5DARQ%2B8upZ4owv8MLtv%2BaxXhs1gCsoQpSS%2BcDLagX4z3QMBk%2FoZocaway8MFNzx20DLR5V2QynIRAw0DaZ18%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240319T192859Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY4Y5ALIEK%2F20240319%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=4849c5370f578172c916d61dfab2d57fdc7e22e4be1c27ac6520ab61122135c6&hash=81657ba33604f7785b6915163ab87d523ebc6cb07c6758ab276b62ba41a73d8b&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S2352340921002870&tid=spdf-ee63ed9f-4ae0-4bc3-9928-7daf11712e89&sid=e075e776976bf64cbf5a86e239b9a216a04fgxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=18165c535501020a5453&rr=866fde641e14011e&cc=br
-->

<br>

<p align = "justify">
The inverse problem is a form of modelating problems which allow defining the parameters of the analyzed system based on a given data set. For example, it is possible to know the characteristics of a harmonic oscillator system (like the stiffness) just knowing a certain quantity of positions of the mass given through time. Larger data sets mean more accuracy to the value prediction.
Taking for example a signal given by a simple equation like:
</p>

$$y(t)=acos(bt)$$

<p align = "justify">
Taking a=3 and b=4 results in the following graphic:
</p>

<p align = "center">
<img src="assets/images/exemp_orig.png" />
</p>

<p align = "justify">
Now, add some noise to the signal (10%), making it similar to what an experimentally obtained data could be.
</p>

<p align = "center">
<img src="assets/images/exemp_noisy.png" />
</p>

<p align = "justify">
In a real case, the equation that produced this graphic would be unknown. Although, it is possible to assume the equation is probally a cosine function due to its form, and so to get back the values of the parameters (in this case, <i>a</i> and <i>b</i>) by using an optimization algorithm, which will optimize the loss function (MSE) that describes how far our prediction is from the real values of the parameters.
</p>

$${OF =\frac{1}{n} \sum^n_{i=0}(y_{pred}^{(i)} - y_{exp}^{(i)})^2}$$

<p align = "justify">
Where n is the number of points in the data set, y_{exp} is the y value of the i_th experimentally given point, and y_{pred} is the y value of the i-th given by the equation using the predicted parameters.
Basically, the concept is about trying to "guess" which values of wanted parameters can lead to the better aproximation to the results of the experiment. There are several methods to "guess" the parameter values.
Solving this example using genetic algorithm, setting a population=50 and 100 max iterations, the following solution appears: a=2.9884694436445205 and b=4.001254870797622, that is a good approximation of the original values of 3 and 4, respectively.
</p>

<p align = "center">
<img src="assets/images/exemp_comparison.png" />
</p>

<p align = "justify">
In this application, the optimization technique is used to minimize the deviation between the numerical results and the ones observed experimentally <a href="#ref1">[1]</a>, where the Objective Function (OF) is given by equation <a href="#eq1">(1)</a>.
</p>

<table border = "0" style = "width:100%">
    <tr>
        <td style="width: 90%;">\[ min \left| \mathbf{y}_{\text{true}} - \mathbf{y}_{\text{pred}} \right| \]</td>
        <td style="width: 10%;"><p align = "right" id = "eq1">(1)</p></td>
    </tr>
</table>

<p align = "justify">
The section <a target="_blank" rel="noopener" href="https://wmpjrufg.github.io/METAPY/STATS_LOSS.html">"loss"</a> shows some loss equations implemented in the METApy framework.
</p>

<h3>Reference list</h3>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Reference</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><p align = "center" id = "ref1">[1]</p></td>
            <td><p align = "left"><a href="https://link.springer.com/article/10.1007/s13369-022-07132-6" target="_blank" rel="noopener noreferrer">Pereira Junior, W.M.; Borges, R.A.; Araújo, D.L; Fernandes, G. R.; Pituba, J. J. C. (2023). Parametric Identification and Sensitivity Analysis Combined with a Damage Model for Reinforced Concrete Structures. Arab J Sci Eng 48, 4751–4767</a></p></td>
        </tr>
    </tbody>
</table>
