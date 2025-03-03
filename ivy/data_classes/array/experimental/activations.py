# global
import abc
from typing import Optional, Union, Literal

# local
import ivy


class _ArrayWithActivationsExperimental(abc.ABC):
    def logit(
        self,
        /,
        *,
        eps: Optional[float] = None,
        complex_mode: Literal["split", "magnitude", "jax"] = "jax",
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.logit. This method simply wraps the
        function, and so the docstring for ivy.logit also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            Input array.
        eps
            When eps is None the function outpus NaN where x < 0 or x > 1.
            and inf or -inf where x = 1 or x = 0, respectively.
            Otherwise if eps is defined, x is clamped to [eps, 1 - eps]
        complex_mode
            optional specifier for how to handle complex data types. See
            ``ivy.func_wrapper.handle_complex_input`` for more detail.
        out
            Optional output array.

        Returns
        -------
        ret
            Array containing elementwise logits of x.

        Examples
        --------
        >>> x = ivy.array([1, 0, 0.9])
        >>> z = x.logit()
        >>> print(z)
        ivy.array([       inf,       -inf, 2.19722438])

        >>> x = ivy.array([1, 2, -0.9])
        >>> z = x.logit(eps=0.2)
        >>> print(z)
        ivy.array([ 1.38629448,  1.38629448, -1.38629436])
        """
        return ivy.logit(self, eps=eps, complex_mode=complex_mode, out=out)

    def thresholded_relu(
        self: ivy.Array,
        /,
        *,
        threshold: Union[int, float] = 0,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.thresholded_relu. This method simply
        wraps the function, and so the docstring for ivy.thresholded_relu also applies
        to this method with minimal changes.

        Parameters
        ----------
        self
            input array.
        threshold
            threshold value above which the activation is linear. Default: ``0``.
        out
            optional output array, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            an array with the relu activation function applied element-wise
            with custom threshold.

        Examples
        --------
        >>> x = ivy.array([-1., .2, 1.])
        >>> y = x.thresholded_relu(threshold=0.5)
        >>> print(y)
        ivy.array([0., 0., 1.])
        """
        return ivy.thresholded_relu(self._data, threshold=threshold, out=out)

    def prelu(
        self,
        slope: Union[float, ivy.NativeArray, ivy.Array],
        /,
        *,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        Prelu takes input data (Array) and slope array as input,

        and produces one output data (array) where the function
        f(x) = slope * x for x < 0, f(x) = x for x >= 0., is applied
        to the data array elementwise. This operator supports unidirectional
        broadcasting (array slope should be unidirectional broadcastable to
        input tensor X);

        Parameters
        ----------
        self
            input array.
        slope
            Slope Array. The shape of slope can be smaller than first input X;
            if so, its shape must be unidirectional broadcastable to X.
        out
            Optional output array.

        Returns
        -------
        ret
            input array with prelu applied elementwise.
        """
        return ivy.prelu(self._data, slope, out=out)

    def relu6(
        self,
        /,
        *,
        complex_mode: Literal["split", "magnitude", "jax"] = "jax",
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        Apply the rectified linear unit 6 function element-wise.

        Parameters
        ----------
        self
            input array
        complex_mode
            optional specifier for how to handle complex data types. See
            ``ivy.func_wrapper.handle_complex_input`` for more detail.
        out
            optional output array, for writing the result to.
            It must have a shape that the inputs broadcast to.

        Returns
        -------
        ret
            an array containing the rectified linear unit 6 activation
            of each element in input.

        Examples
        --------
        With :class:`ivy.Array` input:

        >>> x = ivy.array([-1.,  0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.])
        >>> y = ivy.relu6(x)
        >>> print(y)
        ivy.array([0., 0., 1., 2., 3., 4., 5., 6., 6.])

        >>> x = ivy.array([-1.,  0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.])
        >>> y = ivy.zeros(9)
        >>> ivy.relu6(x, out = y)
        >>> print(y)
        ivy.array([0., 0., 1., 2., 3., 4., 5., 6., 6.])
        """
        return ivy.relu6(self._data, complex_mode=complex_mode, out=out)

    def logsigmoid(
        self: ivy.Array,
        complex_mode: Literal["split", "magnitude", "jax"] = "jax",
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.logsigmoid. This method simply wraps
        the function, and so the docstring for ivy.logsigmoid also applies to this
        method with minimal changes.

        Parameters
        ----------
        self
            Input array.
        complex_mode
            optional specifier for how to handle complex data types. See
            ``ivy.func_wrapper.handle_complex_input`` for more detail.

        Returns
        -------
            Array with same shape as input with Log-sigmoid applied to every element.

        Examples
        --------
        >>> x = ivy.array([-1., 2., 4., -10.])
        >>> z = x.logsigmoid()
        >>> print(z)
        ivy.array([ -1.31326175,  -0.126928  ,  -0.01814993, -10.00004578])

        >>> x = ivy.array([-2.5, 1., 0, 4.5])
        >>> z = x.logsigmoid()
        >>> print(z)
        ivy.array([-2.57888985, -0.31326169, -0.69314718, -0.01104775])
        """
        return ivy.logsigmoid(self._data, complex_mode=complex_mode)

    def selu(self, /, *, out: Optional[ivy.Array] = None) -> ivy.Array:
        """
        Apply the scaled exponential linear unit function element-wise.

        Parameters
        ----------
        self
            input array
        out
            optional output array, for writing the result to.
            It must have a shape that the inputs broadcast to.

        Returns
        -------
        ret
            an array containing the scaled exponential linear unit activation
            of each element in input.

        Examples
        --------
        With :class:`ivy.Array` input:

        >>> x = ivy.array([-1.,  0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.])
        >>> y = x.selu()
        >>> print(y)
        ivy.array([-1.11133075,  0.,  1.05070102,  2.10140204,  3.15210295,
                    4.20280409,  5.25350523,  6.30420589,  7.35490704])

        >>> x = ivy.array([-1.,  0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.])
        >>> y = ivy.zeros(9)
        >>> x.selu(out = y)
        >>> print(y)
        ivy.array([-1.11133075,  0.,  1.05070102,  2.10140204,  3.15210295,
                    4.20280409,  5.25350523,  6.30420589,  7.35490704])
        """
        return ivy.selu(self._data, out=out)

    def silu(self: ivy.Array, /, *, out: Optional[ivy.Array] = None) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.silu. This method simply wraps the
        function, and so the docstring for ivy.silu also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            input array.
        out
            optional output array, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Examples
        --------
        >>> x = ivy.array([-1., 0., 1.])
        >>> y = x.silu()
        >>> print(y)
        ivy.array([-0.26894143,  0.        ,  0.73105854])
        """
        return ivy.silu(self._data, out=out)

    def elu(
        self,
        /,
        *,
        alpha: float = 1.0,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        Ivy.Array instance method variant of ivy.elu. This method simply wraps the
        function, and so the docstring for ivy.elu also applies to this method with
        minimal.

        Parameters
        ----------
        self
            input array.
        alpha
            scaler for controlling the slope of the function for x <= 0 Default: 1.0
        out
            optional output array, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            an array with the elu activation function applied element-wise.

        Examples
        --------
        >>> x = ivy.array([0.39, -0.85])
        >>> y = x.elu()
        >>> print(y)
        ivy.array([ 0.39, -0.57])
        """
        return ivy.elu(self._data, alpha=alpha, out=out)

    def hardtanh(
        self: ivy.Array,
        /,
        *,
        max_val: float = 1,
        min_val: float = -1,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.hardtanh. This method simply wraps the
        function, and so the docstring for ivy.hardtanh also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            input array.
        min_val
            minimum value of the linear region range. Default: -1.
        max_val
            maximum value of the linear region range. Default: 1.
        out
            optional output array, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            an array with the hardtanh activation function applied element-wise
            with custom linear region range.

        Examples
        --------
        >>> x = ivy.array([-1., .2, 1.])
        >>> y = x.hardtanh()
        >>> print(y)
        ivy.array([-1., 1., 1.])
        """
        return ivy.hardtanh(self._data, min_val=min_val, max_val=max_val, out=out)

    def tanhshrink(self: ivy.Array, /, *, out: Optional[ivy.Array] = None) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.tanhshrink. This method simply wraps
        the function, and so the docstring for ivy.tanhshrink also applies to this
        method with minimal changes.

        Parameters
        ----------
        self
            input array.
        out
            optional output array, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Examples
        --------
        >>> x = ivy.array([-1., 0., 1.])
        >>> y = x.tanhshrink()
        >>> print(y)
        ivy.array([-0.23840582,  0.        ,  0.23840582])
        """
        return ivy.tanhshrink(self._data, out=out)

    def celu(
        self: ivy.Array,
        /,
        *,
        alpha: float = 1.0,
        complex_mode: Literal["split", "magnitude", "jax"] = "jax",
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.celu. This method simply wraps the
        function, and so the docstring for ivy.celu also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            input array.
        alpha
            the alpha (negative slope) value for CELU formulation.
        complex_mode
            optional specifier for how to handle complex data types. See
            ``ivy.func_wrapper.handle_complex_input`` for more detail.
        out
            optional output array, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            an array with the celu activation function applied element-wise.

        Examples
        --------
        >>> x = ivy.array([0.39, -0.85])
        >>> y = x.celu()
        >>> print(y)
        ivy.array([ 0.39, -0.57])
        """
        return ivy.celu(self._data, alpha=alpha, complex_mode=complex_mode, out=out)
