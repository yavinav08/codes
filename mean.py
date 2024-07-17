if axis not in [0, 1, 2]:
        raise ValueError("Axis must be 0, 1, or 2")

    if axis == 0:
        # Mean over items
        result = self.apply(lambda x: x.mean(), axis=1)
        return result

    elif axis == 1:
        # Mean over major_axis
        result = self.apply(lambda x: x.mean(), axis=0).unstack(level='minor_axis')
        if result.index.dtype == 'float64':
            result.index = result.index.astype(object)
        return result

    elif axis == 2:
        # Mean over minor_axis
        result = self.stack().groupby(level='major_axis').mean().unstack()
        if result.index.dtype == 'float64':
            result.index = result.index.astype(object)
        return result
