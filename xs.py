def xs(self, key, axis=0):
    """
    Return cross-section from the CustomPanel.

    Parameters:
    key: The label or index to select along the given axis.
    axis: Axis along which to extract the cross-section. 0 for items, 1 for major_axis, 2 for minor_axis.

    Returns:
    pd.DataFrame: Cross-section along the specified axis.
    """
    if axis not in [0, 1, 2]:
        raise ValueError("Axis must be 0, 1, or 2")
    
    if axis == 0:
        # Extracting cross-section along items
        result = self.loc[:, key]
    elif axis == 1:
        # Extracting cross-section along major_axis
        result = self.loc[(key, slice(None)), :]
    elif axis == 2:
        # Extracting cross-section along minor_axis
        result = self.loc[(slice(None), key), :]

    return result
