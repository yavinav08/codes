 if items is not None:
            # Reindexing columns (items)
            reindexed_columns = super(CustomPanel, self).reindex(columns=items)
            if method is not None:
                reindexed_columns = reindexed_columns.ffill(axis=1) if method in ['pad', 'ffill'] else \
                                    reindexed_columns.bfill(axis=1) if method in ['backfill', 'bfill'] else \
                                    reindexed_columns.apply(lambda col: col.interpolate(method='nearest') if col.isna().any() else col, axis=1)
            self = reindexed_columns.fillna(fill_value)
