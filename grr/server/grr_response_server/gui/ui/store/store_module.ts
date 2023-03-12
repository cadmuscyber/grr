import {NgModule} from '@angular/core';
import {EffectsModule} from '@ngrx/effects';
import {StoreModule, StoreRootModule} from '@ngrx/store';
import {UserEffects} from '@app/store/user/user_effects';

import {ApiModule} from '../lib/api/module';

import {ClientEffects} from './client/client_effects';
import {clientReducer} from './client/client_reducers';
import {CLIENT_FEATURE} from './client/client_selectors';
import {ClientFacade} from './client_facade';
import {ClientSearchEffects} from './client_search/client_search_effects';
import {clientSearchReducer} from './client_search/client_search_reducers';
import {CLIENT_SEARCH_FEATURE} from './client_search/client_search_selectors';
import {ClientSearchFacade} from './client_search_facade';
import {FlowEffects} from './flow/flow_effects';
import {flowReducer} from './flow/flow_reducers';
import {FLOW_FEATURE} from './flow/flow_selectors';
import {FlowFacade} from './flow_facade';
import {userReducer} from './user/user_reducers';
import {USER_FEATURE} from './user/user_selectors';
import {UserFacade} from './user_facade';

/**
 * Root NgRx store definition.
 */
@NgModule({
  imports: [
    ApiModule,
    StoreModule.forRoot({}, {
      runtimeChecks: {
        // TODO(user): limit to dev mode only.
        strictStateImmutability: true,
        strictActionImmutability: true,
      },
    }),
    StoreModule.forFeature(CLIENT_SEARCH_FEATURE, clientSearchReducer),
    StoreModule.forFeature(CLIENT_FEATURE, clientReducer),
    StoreModule.forFeature(FLOW_FEATURE, flowReducer),
    StoreModule.forFeature(USER_FEATURE, userReducer),
    EffectsModule.forRoot([
      ClientSearchEffects,
      ClientEffects,
      FlowEffects,
      UserEffects,
    ]),
  ],
  providers: [
    ClientSearchFacade,
    ClientFacade,
    FlowFacade,
    UserFacade,
  ],
  exports: [StoreRootModule]
})
export class GrrStoreModule {
}
