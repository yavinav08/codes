if items is not None:
        # Create an empty DataFrame with the new items
        new_columns = pd.DataFrame(index=self.index, columns=items)

        # Use the original data to fill the new DataFrame
        reindexed_columns = new_columns.combine_first(self)

        # Apply the specified fill method
        if method in ['pad', 'ffill']:
            reindexed_columns = reindexed_columns.ffill(axis=1)
        elif method in ['backfill', 'bfill']:
            reindexed_columns = reindexed_columns.bfill(axis=1)
        elif method == 'nearest':
            reindexed_columns = reindexed_columns.apply(
                lambda col: col.interpolate(method='nearest') if col.isna().any() else col, axis=1)

        # Fill remaining NaN values with fill_value
        if fill_value is not None:
            reindexed_columns = reindexed_columns.fillna(fill_value)

        # Drop columns not in the new items
        reindexed_columns = reindexed_columns.loc[:, items]

        # Return new CustomPanel with reindexed columns
        return CustomPanel(reindexed_columns)
