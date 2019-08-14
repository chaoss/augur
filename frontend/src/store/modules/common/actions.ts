import Repo from '@/AugurAPI';
import RepoGroup from '@/AugurAPI';
export default {
    async createAPIObjects(context: any, payload: any) {
        try {
            const apiGroups = context.state.getRepoGroups || {};
            const apiRepos = context.state.getRepos || {};
            console.log('DOING IT')
            if ('repos' in payload) {
                payload.repos.forEach((repo: any) => {
                    apiRepos[repo.url] = context.state.AugurAPI.Repo({gitURL: repo.url,
                        repo_id: repo.repo_id})
                })
            }
            if ('groups' in payload) {
                payload.groups.forEach((group: any) => {
                    apiGroups[group.rg_name] = context.state.AugurAPI.RepoGroup({rg_name:
                        group.rg_name, repo_group_id: group.repo_group_id})
                })
            }
            context.commit('update_properties', {
                property: 'apiRepos',
                with: apiRepos,
            });
            context.commit('update_properties', {
                property: 'apiGroups',
                with: apiGroups,
            });
        } catch (error) {
            throw error;
        }
    },
    async endpoint(context: any, payload: any) {
        try {
            return new Promise((resolve, reject) => {
                let tempCache = context.state.cache || {};
                if ('endpoints' in payload) {
                    if ('repos' in payload) {
                        context.state.AugurAPI.batchMapped(payload.repos, payload.endpoints).then(
                            (data: object[]) => {
                                console.log(data)
                                tempCache = {...tempCache, ...data};
                                payload.repos.forEach((repo: any) => {
                                    tempCache[repo.toString()] = {...tempCache[repo.toString()], ...data[repo.toString()]};
                                });
                                console.log(tempCache)
                                resolve(tempCache)
                            });
                    }
                    if ('repoGroups' in payload) {
                        context.state.AugurAPI.batchMapped(payload.repoGroups, payload.endpoints).then(
                            (data: object[]) => {
                                tempCache = {...tempCache, ...data};
                                payload.repoGroups.forEach((group: any) => {
                                    tempCache[group.rg_name] = {...tempCache[group.rg_name],
                                        ...data[group.rg_name]};
                                });
                                console.log(tempCache)
                                resolve(tempCache)
                            });
                    }
                    if (!('repos' in payload) && !('repoGroups' in payload)) {
                        payload.endpoints.forEach((endpoint: string) => {
                            console.log(endpoint)
                            context.state.AugurAPI[endpoint]().then((data: object[]) => {
                                tempCache[endpoint] = data;
                                console.log(tempCache)
                                resolve(tempCache)
                            });
                        });
                    }
                }
                // console.log(tempCache)
                // resolve(tempCache)
                // context.commit('mutate', {
                //     property: 'cache',
                //     with: tempCache,
                // });
                // resolve(tempCache)
            });
        } catch (error) {
            throw error;
        }
    },
    async loadRepos(context: any, payload: any) {
        try {
            return new Promise((resolve, reject) => {
                context.state.AugurAPI.getRepos().then((repos: object[]) => {
                    context.commit('mutateCache', {
                        property: 'getRepos',
                        with: repos,
                    });
                    resolve(repos)
                });
            })
        } catch (error) {
            throw error;
        }
    },
    async loadRepoGroups(context: any, payload: any) {
        try {
            return new Promise((resolve, reject) => {
                context.state.AugurAPI.getRepoGroups().then((rgs: object[]) => {
                    context.commit('mutateCache', {
                        property: 'getRepoGroups',
                        with: rgs,
                    });
                    resolve(rgs)
                });
            })
        } catch (error) {
            throw error;
        }
    },
    // async loadRepoRelations(context:any, payload:any){
    //     try {

    //         context.dispatch('loadRepoGroups').then(() => {
    //             context.state.getters.repoGroups.forEach((group: any): void => {
    //                 repoGroups[group.rg_name] = group
    //                 repoRelations[group.rg_name] = {};
    //                 repos.filter((repo: any) => {
    //                     return repo.rg_name === group.rg_name;
    //                 }).forEach((repo: any) => {
    //                     repoRelations[group.rg_name][repo.url] = repo
    //                 });
    //             });
    //             context.commit('mutateCache', {
    //                 property: 'repoRelations',
    //                 with: repoRelations,
    //             });
    //         })
    //     } catch(error) {
    //         throw error;
    //     }
    // },
    // getRepoRelations(context: any, payload: object) {
    //     return new Promise ((resolve, reject) => {
    //         setTimeout(() => {
    //             let repoRelations = context.state.cache.getRepos || {};
    //             let repoGroups = context.state.cache.getRepoGroups || {};
    //             context.state.AugurAPI.getRepos().then((repos: object[]) => {
    //                 context.state.AugurAPI.getRepoGroups().then((groups: object[]) => {
    //                     // Move down between future relation endpoint
    //                     groups.forEach((group: any): void => {
    //                         repoGroups[group.rg_name] = group
    //                         repoRelations[group.rg_name] = {};
    //                         repos.filter((repo: any) => {
    //                             return repo.rg_name === group.rg_name;
    //                         }).forEach((repo: any) => {
    //                             repoRelations[group.rg_name][repo.url] = repo
    //                         });
    //                     });
    //                     context.commit('mutateCache', {
    //                         property: 'repoRelations',
    //                         with: repoRelations,
    //                     });
    //                     context.commit('mutateCache', {
    //                         property: 'repoGroups',
    //                         with: repoGroups,
    //                     });
    //                 });
    //             resolve({ repoRelations, repoGroups });
    //             });
    //         }, 2000)
    //     })
    // },
    async addRepo(context: any, payload: any) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                const rgName = payload.rg_name || undefined
                const repoName = payload.repo_name || undefined
                const repoId = payload.repo_id || undefined
                const repoGroupId = payload.repo_group_id || undefined
                const gitURL = payload.url || undefined

                const repo: Repo = context.state.AugurAPI.Repo({
                    '{gitURL}': gitURL,
                    '{repo_id}': repoId,
                    'repo_group_id': repoGroupId,
                    'rg_name': rgName,
                    '{repo_name}': repoName,
                })
                context.commit('mutateAPIRepo', { '{repo}': repo, 'name': repo.toString()})
                resolve(repo)
            }, 2000)
        })
    },
    async addRepoGroup(context: any, payload: any) {
        return new Promise((resolve, reject) => {
            const rgName = payload.rg_name || undefined
            const repoGroupId = payload.repo_group_id || undefined
            const group: RepoGroup = context.state.AugurAPI.RepoGroup({'{repo_group_id}': repoGroupId, '{rg_name}': rgName})

            context.commit('mutateAPIGroup', {'{group}': group, '{rg_name}': rgName})
        })
    },
};
